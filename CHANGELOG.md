# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog] and this project adheres to [Semantic Versioning].

<!--
GitHub MD Syntax:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Highlighting:
https://docs.github.com/assets/cb-41128/mw-1440/images/help/writing/alerts-rendered.webp

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.
-->

## [In Development] - Unreleased

<!--
Section Order:

### Added
### Fixed
### Changed
### Deprecated
### Removed
### Security
-->

<!-- Your changes go here -->

### Changed

- Switched to DataTables 2
- ESI handling improved. This should save a bunch of ESI calls when processing fleets.

## [3.0.1] - 2025-11-12

### Changed

- Dependency to `django-esi` set to `>=8.0.0,<9` (for real this time …)

## [3.0.0] - 2025-11-12

### Fixed

- Django `makemessages` doesn't seem to recognise f-strings anymore
- Use translated name as menu item

### Changed

- Switched to OpenAPI3 specification for ESI endpoints
  - Dependency to `django-esi` set to `>=8.0.0,<9`
  - Set compatibility date to 2025-11-06 (November 6th, 2025)
- Set the maximum required Python version to 3.13
- Better way of re-raising an exception in the `get_fleet_composition` task
- Translations updated

## [3.0.0-beta.2] - 2025-11-04

> [!CAUTION]
>
> This is a BETA version, not intended for production use!
> Please test it in a safe environment first and [report any issues you find](https://github.com/ppfeufer/aa-fleetfinder/issues).
>
> This version is pulling in an BETA version of `django-esi` as well,
> so please be aware that this might break at any time.

### Fixed

- Use translated name as menu item

### Changed

- Better way of re-raising an exception in the `get_fleet_composition` task
- Dependency to `django-esi` set to `>=8.0.0-beta.2`

## [3.0.0-beta.1] - 2025-10-23

> [!CAUTION]
>
> This is a BETA version, not intended for production use!
> Please test it in a safe environment first and [report any issues you find](https://github.com/ppfeufer/aa-fleetfinder/issues).
>
> This version is pulling in an BETA version of `django-esi` as well,
> so please be aware that this might break at any time.

### Fixed

- Django `makemessages` doesn't seem to recognise f-strings anymore

### Changed

- Switched to OpenAPI3 specification for ESI endpoints
  - Set compatibility date to 2025-09-30 (September 30, 2025)
- Set the maximum required Python version to 3.13

## [2.7.2] - 2025-10-07

### Changed

- Translations updated

## [2.7.1] - 2025-08-23

### Added

- Header to fleet details view (Fleet name and FC name)
- More error handling in fleet details view

### Changed

- Inline JavaScript moved to separate files
- Switch to Terser for JavaScript compression
- Set chunk size for ESI calls to `Universe.post_universe_names` to 1000 to match the
  limit for this endpoint (Thanks to @cvweiss (Squizz Caphinator) for pointing this out)

## [2.7.0] - 2025-08-21

### Added

- A little explanation to the fleet invite form
- Ability to kick a fleet member
- Fleet boss detection

### Fixed

- Slim Select field styling

### Changed

- Resolve IDs to names in chunks of a maximum of 500
- `views.ajax_dashboard` refactored
- Dashboard buttons to Font Awesome icons
- Dashboard JS refactored
- Fleet details JS refactored
- Translations updated

## [2.6.1] - 2025-08-19

### Fixed

- FC can't see their own fleet when not in selected group(s)

### Changed

- `views.ajax_fleet_details` refactored
- `tasks._process_fleet` refactored
- `tasks.open_fleet` refactored
- `tasks.send_fleet_invitation` refactored
- `tasks.check_fleet_adverts` refactored
- `tasks.get_fleet_composition` refactored
- Fleet creation logic refactored, and better error handling added

### Removed

- MOTD from fleet details form, as it cannot be formatted properly and might delete the ingame MOTD when not set

## [2.6.0] - 2025-08-14

### Changed

- Use AA framework JS functions
- Minimum requirements
  - Alliance Auth >= 4.9.0

## [2.5.1] - 2025-08-04

### Changed

- Translations updated

## [2.5.0] - 2025-07-08

### Added

- New dependency
  - `django-esi>=7.0.1`

### Changed

- User Agent generation updated to match latest `django-esi` guidelines

## [2.4.0] - 2025-06-03

### Changed

- Translations updated

### Removed

- Cache breaker for static files. Doesn't work as expected with `django-sri`.

## [2.3.4] - 2025-05-05

### Changed

- Translations updated

## [2.3.3] - 2025-04-09

### Changed

- Moved the navigation to the top nav bar
- Moved the template tag to the `templatetags` module

## [2.3.2] - 2025-03-06

### Changed

- Templatetag code improved
- Omit SRI hash calculation when `DEBUG=True`
- Translations updated

## [2.3.1] - 2025-01-20

### Removed

- Rogue quotation mark

## [2.3.0] - 2025-01-20

### Added

- Integrity hash for the static files
- Cache busting for static files
- Datatable translations

### Changed

- Set user agent according to MDN guidelines
- URLs to be more semantic
- Minimum requirements
  - Alliance Auth >= 4.6.0

## [2.2.2] - 2024-12-14

### Added

- Python 3.13 to the test matrix

### Changed

- Translations updated

## [2.2.1] - 2024-11-01

### Changed

- Italian translation improved
- Ukrainian translation improved

## [2.2.0] - 2024-09-16

### Changed

- Dependencies updated
  - `allianceauth`>=4.3.1
- Japanese translation improved
- Lingua codes updated to match Alliance Auth v4.3.1

## [2.1.0] - 2024-07-27

### Added

- Prepared Czech translation for when Alliance Auth supports it

### Changed

- Chinese translation improved
- French translation improved
- Japanese translation improved
- Russian translation improved

### Removed

- Support for Python 3.8 and Python 3.9

## [2.0.1] - 2024-05-16

### Changed

- Translations updated

## [2.0.0] - 2024-03-16

> [!NOTE]
>
> **This version needs at least Alliance Auth v4.0.0!**
>
> Please make sure to update your Alliance Auth instance **before**
> you install this version, otherwise, an update to Alliance Auth will
> be pulled in unsupervised.

### Added

- Compatibility to Alliance Auth v4
  - Bootstrap 5
  - Django 4.2
- Native lazy loading support for images

### Fixed

- Fleet is being displayed multiple times when multiple group restrictions are in place

### Removed

- Support for Alliance Auth v3

## [2.0.0-beta.1] - 2024-02-18

> [!NOTE]
>
> **This version needs at least Alliance Auth v4.0.0b1!**
>
> Please make sure to update your Alliance Auth instance **before**
> you install this version, otherwise, an update to Alliance Auth will
> be pulled in unsupervised.

### Added

- Compatibility to Alliance Auth v4
  - Bootstrap 5
  - Django 4.2
- Native lazy loading support for images

### Fixed

- Fleet is being displayed multiple times when multiple group restrictions are in place

### Removed

- Support for Alliance Auth v3

## [1.5.2] - 2023-09-26

> [!NOTE]
>
> **This is the last version compatible with Alliance Auth v3.**

### Fixed

- Capitalization for translatable strings

### Changed

- Translations improved and updated
- Test suite updated

## [1.5.1] - 2023-09-02

### Changed

- Korean translation improved

## [1.5.0] - 2023-08-30

### Added

- Korean translation

## [1.4.0] - 2023-08-15

### Added

- Spanish translation

## [1.3.2] - 2023-08-13

### Fixed

- Bootstrap CSS fix

## [1.3.1] - 2023-07-30

### Added

- Footer to promote help with the app translation

### Changed

- Ukrainian translation improved

## [1.3.0] - 2023-06-30

### Changed

- Use Django's native message system instead of forcing our own
- Translations improved
- Task code cleaned up
- Error tracking for ESI fleets moved to the DB instead of being cached by Redis, as
  Redis was too unreliable and there was a good chance the task stopped working
  properly.

## [1.2.0] - 2023-04-25

### Changed

- Moved the build process to PEP 621 / pyproject.toml

## [1.1.0] - 2023-04-16

### Added

- Russian translation

## [1.0.0] - 2023-04-13

### Added

- German translation

## [1.0.0-beta.1] - 2023-01-10

### Changed

- Migrations reset

## [0.1.0-alpha.20] - 2023-01-05

### Fixed

- UTF-8 characters in log message

### Removed

- Auto retry for ESI and OS errors in tasks, since django-esi already retries all
  relevant errors

## [0.1.0-alpha.19] - 2022-09-18

### Changed

- Dashboard error message replaced with Django message API
- Internal improvements

## [0.1.0-alpha.18] - 2022-08-23

### Added

- `related_name` to `fleet_commander` in model

### Changed

- CSS moved to bundled HTML template
- Logger messages changed to f-strings
- Using `allianceauth-app-utils` for logging
- Task ESI error handling improved
- Moved constants to their own file
- `related_name` for group restrictions in the model to prevent conflicts with other
  modules. The name was too generic.
- Minimum Requirements
  - Alliance Auth >= 3.0.0
  - Python >= 3.8

### Removed

- Unused code

## [0.1.0-alpha.17] - 2022-07-11

### Changed

- Switch to f-strings for formatted strings
- Templates cleaned up

## [0.1.0-alpha.16] - 2022-06-24

### Added

- Versioned static template tag

### Removed

- AVOID_CDN setting, we serve always locally (GDPR)

## [0.1.0-alpha.15] - 2022-03-02

### Added

- Test suite for AA 3.x and Django 4

### Removed

- Deprecated settings

### Changed

- Minimum dependencies:
  - Alliance Auth>=2.11.0 (as last stable of the 2.x branch for now)

## [0.1.0-alpha.14] - 2022-03-01

### Removed

- `setup.py` as it is no longer required

### Changed

- Makefile updated

## [0.1.0-alpha.13] - 2022-03-01

### Added

- Package discovery to `setup.cfg` (hopefully)

## [0.1.0-alpha.12] - 2022-03-01

### Fixed

- Classifiers in `setup.cfg`

## [0.1.0-alpha.11] - 2022-03-01

### Changed

- Switched to `setup.cfg` instead of `setup.py`

## [0.1.0-alpha.10] - 2022-02-28

### Fixed

- [Compatibility] AA 3.x / Django 4 :: ImportError: cannot import name
  'ugettext_lazy' from 'django.utils.translation'

## [0.1.0-alpha.9] - 2022-02-02

### Added

- Tests for Python 3.11

### Changed

- Using `path` in URL config instead of soon-to-be removed `url`
- Minimum requirements
  - Alliance Auth v2.9.4

## [0.1.0-alpha.8] - 2021-11-30

### Changed

- Minimum requirements
  - Python 3.7
  - Alliance Auth v2.9.3

## [0.1.0-alpha.7] - 2021-11-15

### Added

- Basic test suite

## [0.1.0-alpha.6] - 2021-07-08

### Changed

- Compatibility with Python 3.9 and Django 3.2

## [0.1.0-alpha.5] - 2021-01-25

### Added

- ESI error hardening

### Changed

- Fleet table on dashboard is now loaded via ajax and refreshed every 30 seconds

## [0.1.0-alpha.4] - 2021-01-12

### Removed

- Django 2 support

## [0.1.0-alpha.3] - 2021-01-05

### Fixed

- Permission to create fleets

## [0.1.0-alpha.2] - 2021-01-05

### Changed

- Datatables in fleet details view set up properly
- UI in fleet details view re-done
- Fleet details are now refreshed every 15 seconds via Datatables reload

## [0.1.0-alpha.1] - 2020-12-30

App forked from [Dreadbomb/aa-fleet]

### Fixed

- HTML errors
- Datatable errors
- Import order
- Code issues cleaned up
- General model and permissions

### Changed

- Fleet commander transformed into EveCharacter model
- Automatic page reload in fleet details view deactivated (was causing troubles)
- Datatable for dashboard configured properly
- Migrations reset

<!-- Links to be updated upon release -->

[0.1.0-alpha.1]: https://github.com/ppfeufer/aa-fleetfinder/commits/v0.1.0-alpha.1 "v0.1.0-alpha.1"
[0.1.0-alpha.10]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.6...v0.1.0-alpha.10 "v0.1.0-alpha.10"
[0.1.0-alpha.11]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.10...v0.1.0-alpha.11 "v0.1.0-alpha.11"
[0.1.0-alpha.12]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.11...v0.1.0-alpha.12 "v0.1.0-alpha.12"
[0.1.0-alpha.13]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.12...v0.1.0-alpha.13 "v0.1.0-alpha.13"
[0.1.0-alpha.14]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.13...v0.1.0-alpha.14 "v0.1.0-alpha.14"
[0.1.0-alpha.15]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.9...v0.1.0-alpha.15 "v0.1.0-alpha.15"
[0.1.0-alpha.16]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.15...v0.1.0-alpha.16 "v0.1.0-alpha.16"
[0.1.0-alpha.17]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.16...v0.1.0-alpha.17 "v0.1.0-alpha.17"
[0.1.0-alpha.18]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.17...v0.1.0-alpha.18 "v0.1.0-alpha.18"
[0.1.0-alpha.19]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.18...v0.1.0-alpha.19 "v0.1.0-alpha.19"
[0.1.0-alpha.2]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.1...v0.1.0-alpha.2 "v0.1.0-alpha.2"
[0.1.0-alpha.20]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.19...v0.1.0-alpha.20 "v0.1.0-alpha.20"
[0.1.0-alpha.3]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.2...v0.1.0-alpha.3 "v0.1.0-alpha.3"
[0.1.0-alpha.4]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.3...v0.1.0-alpha.4 "v0.1.0-alpha.4"
[0.1.0-alpha.5]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.4...v0.1.0-alpha.5 "v0.1.0-alpha.5"
[0.1.0-alpha.6]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.5...v0.1.0-alpha.6 "v0.1.0-alpha.6"
[0.1.0-alpha.7]: https://github.com/ppfeufer/aa-fleetfinder/commits/v0.1.0-alpha.7 "v0.1.0-alpha.7"
[0.1.0-alpha.8]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.7...v0.1.0-alpha.8 "v0.1.0-alpha.8"
[0.1.0-alpha.9]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.8...v0.1.0-alpha.9 "v0.1.0-alpha.9"
[1.0.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.0.0-beta.1...v1.0.0 "v1.0.0"
[1.0.0-beta.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v0.1.0-alpha.20...v1.0.0-beta.1 "v1.0.0-beta.1"
[1.1.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.0.0...v1.1.0 "v1.1.0"
[1.2.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.1.0...v1.2.0 "v1.2.0"
[1.3.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.2.0...v1.3.0 "v1.3.0"
[1.3.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.3.0...v1.3.1 "v1.3.1"
[1.3.2]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.3.1...v1.3.2 "v1.3.2"
[1.4.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.3.2...v1.4.0 "v1.4.0"
[1.5.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.4.0...v1.5.0 "v1.5.0"
[1.5.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.5.0...v1.5.1 "v1.5.1"
[1.5.2]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.5.1...v1.5.2 "v1.5.2"
[2.0.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.5.2...v2.0.0 "v2.0.0"
[2.0.0-beta.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v1.5.2...v2.0.0-beta.1 "v2.0.0-beta.1"
[2.0.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.0.0...v2.0.1 "v2.0.1"
[2.1.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.0.1...v2.1.0 "v2.1.0"
[2.2.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.1.0...v2.2.0 "v2.2.0"
[2.2.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.2.0...v2.2.1 "v2.2.1"
[2.2.2]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.2.1...v2.2.2 "v2.2.2"
[2.3.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.2.2...v2.3.0 "v2.3.0"
[2.3.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.3.0...v2.3.1 "v2.3.1"
[2.3.2]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.3.1...v2.3.2 "v2.3.2"
[2.3.3]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.3.2...v2.3.3 "v2.3.3"
[2.3.4]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.3.3...v2.3.4 "v2.3.4"
[2.4.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.3.4...v2.4.0 "v2.4.0"
[2.5.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.4.0...v2.5.0 "v2.5.0"
[2.5.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.5.0...v2.5.1 "v2.5.1"
[2.6.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.5.1...v2.6.0 "v2.6.0"
[2.6.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.6.0...v2.6.1 "v2.6.1"
[2.7.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.6.1...v2.7.0 "v2.7.0"
[2.7.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.7.0...v2.7.1 "v2.7.1"
[2.7.2]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.7.1...v2.7.2 "v2.7.2"
[3.0.0]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.7.2...v3.0.0 "v3.0.0"
[3.0.0-beta.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.7.2...v3.0.0-beta.1 "v3.0.0-beta.1"
[3.0.0-beta.2]: https://github.com/ppfeufer/aa-fleetfinder/compare/v2.7.2...v3.0.0-beta.2 "v3.0.0-beta.2"
[3.0.1]: https://github.com/ppfeufer/aa-fleetfinder/compare/v3.0.0...v3.0.1 "v3.0.1"
[dreadbomb/aa-fleet]: https://github.com/Dreadbomb/aa-fleet "Dreadbomb/aa-fleet"
[in development]: https://github.com/ppfeufer/aa-fleetfinder/compare/v3.0.1...HEAD "In Development"
[keep a changelog]: http://keepachangelog.com/ "Keep a Changelog"
[semantic versioning]: http://semver.org/ "Semantic Versioning"
