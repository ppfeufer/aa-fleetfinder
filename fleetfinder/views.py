from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.template.defaulttags import register

from esi.decorators import token_required

from fleetfinder.app_settings import avoid_cdn
from fleetfinder.tasks import (
    open_fleet,
    send_fleet_invitation,
    get_fleet_composition,
)
from fleetfinder.models import Fleet

from bravado.exception import HTTPNotFound

from allianceauth.eveonline.models import EveCharacter
from allianceauth.groupmanagement.models import AuthGroup


@login_required()
@permission_required("fleetfinder.access_fleetfinder")
def dashboard(request):
    groups = request.user.groups.all()
    fleets = Fleet.objects.filter(Q(groups__group__in=groups) | Q(groups=None)).all()

    context = {
        "fleets": fleets,
        "avoid_cdn": avoid_cdn(),  # AVOID_CDN setting
    }

    if "error_edit_fleet" in request.session:
        context["error"] = request.session["error_edit_fleet"].get("error", "")

        del request.session["error_edit_fleet"]

    return render(request, "fleetfinder/dashboard.html", context)


@login_required()
@permission_required("fleetfinder.manage_fleets")
@token_required(
    scopes=(
        "esi-fleets.read_fleet.v1",
        "esi-fleets.write_fleet.v1",
    )
)
def create_fleet(request, token):
    if request.method == "POST":
        auth_groups = AuthGroup.objects.filter(internal=False).all()

        if "modified_fleet_data" in request.session:
            ctx = {}
            ctx["error"] = request.session["modified_fleet_data"].get("error", "")
            ctx["motd"] = request.session["modified_fleet_data"].get("motd", "")
            ctx["name"] = request.session["modified_fleet_data"].get("name", "")
            ctx["groups"] = request.session["modified_fleet_data"].get("groups", "")
            ctx["is_free_move"] = request.session["modified_fleet_data"].get(
                "free_move", ""
            )
            ctx["character_id"] = token.character_id
            ctx["auth_groups"] = auth_groups

            del request.session["modified_fleet_data"]
        else:
            ctx = {"character_id": token.character_id, "auth_groups": auth_groups}

        # AVOID_CDN setting
        ctx["avoid_cdn"] = avoid_cdn()

        return render(request, "fleetfinder/create_fleet.html", context=ctx)

    return redirect("fleetfinder:dashboard")


@login_required()
@permission_required("fleetfinder.manage_fleets")
def edit_fleet(request, fleet_id):
    fleet = Fleet.objects.get(fleet_id=fleet_id)
    auth_groups = AuthGroup.objects.filter(internal=False)

    ctx = {
        "character_id": fleet.fleet_commander_id,
        "auth_groups": auth_groups,
        "fleet": fleet,
        "avoid_cdn": avoid_cdn(),  # AVOID_CDN setting
    }

    return render(request, "fleetfinder/edit_fleet.html", context=ctx)


@login_required()
@permission_required("fleetfinder.access_fleetfinder")
def join_fleet(request, fleet_id):
    ctx = {}
    groups = request.user.groups.all()
    fleet = Fleet.objects.filter(
        Q(groups__group__in=groups) | Q(groups=None), fleet_id=fleet_id
    ).count()

    if fleet == 0:
        return redirect("fleetfinder:dashboard")

    if request.method == "POST":
        character_ids = request.POST.getlist("character_ids", [])
        send_fleet_invitation.delay(character_ids, fleet_id)

        return redirect("fleetfinder:dashboard")
    else:
        characters = (
            EveCharacter.objects.filter(character_ownership__user=request.user)
            .select_related()
            .order_by("character_name")
        )
        ctx["characters"] = characters

    # AVOID_CDN setting
    ctx["avoid_cdn"] = avoid_cdn()

    return render(request, "fleetfinder/join_fleet.html", context=ctx)


@login_required()
@permission_required("fleetfinder.manage_fleets")
def save_fleet(request):
    if request.method == "POST":
        free_move = request.POST.get("free_move", False)

        if free_move == "on":
            free_move = True

        motd = request.POST.get("motd", "")
        name = request.POST.get("name", "")
        groups = request.POST.getlist("groups", [])

        try:
            open_fleet(request.POST["character_id"], motd, free_move, name, groups)
        except HTTPNotFound as ex:
            if request.POST.get("origin", "") == "edit":
                # Here ccp return character not in fleet. Instead push our own message to be clearer
                request.session["error_edit_fleet"] = {
                    "error": "Fleet advert is no longer valid"
                }

                return redirect("fleetfinder:dashboard")

            if request.POST.get("origin", "") == "create":
                request.session["modified_fleet_data"] = {
                    "error": ex.swagger_result["error"],
                    "motd": motd,
                    "name": name,
                    "free_move": free_move,
                    "groups": groups,
                }

                return redirect("fleetfinder:create_fleet")

    return redirect("fleetfinder:dashboard")


@login_required()
@permission_required("fleetfinder.manage_fleets")
def fleet_details(request, fleet_id):
    fleet = get_fleet_composition(fleet_id)

    ctx = {
        "fleet": fleet,
        "avoid_cdn": avoid_cdn(),  # AVOID_CDN setting
    }

    return render(request, "fleetfinder/fleet_details.html", context=ctx)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
