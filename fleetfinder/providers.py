"""
Providers
"""

# Alliance Auth
from esi.clients import EsiClientProvider

# AA Fleet Finder
from fleetfinder import __version__
from fleetfinder.constants import APP_NAME_USERAGENT, GITHUB_URL

# ESI client
esi = EsiClientProvider(
    ua_appname=APP_NAME_USERAGENT, ua_version=__version__, ua_url=GITHUB_URL
)
