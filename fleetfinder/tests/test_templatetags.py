"""
Test the apps' template tags
"""

# Django
from django.template import Context, Template
from django.test import TestCase, override_settings

# AA Fleet Finder
from fleetfinder import __version__
from fleetfinder.constants import PACKAGE_NAME
from fleetfinder.helper.static_files import calculate_integrity_hash


class TestVersionedStatic(TestCase):
    """
    Test the `fleetfinder_static` template tag
    """

    @override_settings(DEBUG=False)
    def test_versioned_static(self):
        """
        Test should return the versioned static

        :return:
        :rtype:
        """

        context = Context(dict_={"version": __version__})
        template_to_render = Template(
            template_string=(
                "{% load fleetfinder %}"
                "{% fleetfinder_static 'css/fleetfinder.min.css' %}"
            )
        )

        rendered_template = template_to_render.render(context=context)

        expected_static_css_src = (
            f'/static/{PACKAGE_NAME}/css/fleetfinder.min.css?v={context["version"]}'
        )
        expected_static_css_src_integrity = calculate_integrity_hash(
            "css/fleetfinder.min.css"
        )

        self.assertIn(member=expected_static_css_src, container=rendered_template)
        self.assertIn(
            member=expected_static_css_src_integrity, container=rendered_template
        )

    @override_settings(DEBUG=True)
    def test_versioned_static_with_debug_enabled(self) -> None:
        """
        Test versioned static template tag with DEBUG enabled

        :return:
        :rtype:
        """

        context = Context({"version": __version__})
        template_to_render = Template(
            template_string=(
                "{% load fleetfinder %}"
                "{% fleetfinder_static 'css/fleetfinder.min.css' %}"
            )
        )

        rendered_template = template_to_render.render(context=context)

        expected_static_css_src = (
            f'/static/{PACKAGE_NAME}/css/fleetfinder.min.css?v={context["version"]}'
        )

        self.assertIn(member=expected_static_css_src, container=rendered_template)
        self.assertNotIn(member="integrity=", container=rendered_template)

    @override_settings(DEBUG=False)
    def test_invalid_file_type(self) -> None:
        """
        Test should raise a ValueError for an invalid file type

        :return:
        :rtype:
        """

        context = Context({"version": __version__})
        template_to_render = Template(
            template_string=(
                "{% load fleetfinder %}"
                "{% fleetfinder_static 'invalid/invalid.txt' %}"
            )
        )

        with self.assertRaises(ValueError):
            template_to_render.render(context=context)
