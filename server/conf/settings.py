r"""
Evennia settings file.

The available options are found in the default settings file found
here:

/usr/src/game/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "C.O.D.E.S."
# Short one-sentence blurb describing your game. Shown under the title
# on the website and could be used in online listings of your game etc.
GAME_SLOGAN = "Chronicles of Darkness - Evennia Support"

######################################################################
# Evennia components
######################################################################

# Global and Evennia-specific apps. This ties everything together so we can
# refer to app models and perform DB syncs.
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.flatpages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "sekizai",
    "evennia.utils.idmapper",
    "evennia.server",
    "evennia.typeclasses",
    "evennia.accounts",
    "evennia.objects",
    "evennia.comms",
    "evennia.help",
    "evennia.scripts",
    "evennia.web.website",
    "evennia.web.webclient",
    "codes.web.advantages",
    "codes.web.arcana",
    "codes.web.auspices",
    "codes.web.clans",
    "codes.web.contracts",
    "codes.web.coils",
    "codes.web.covenants",
    "codes.web.cruac",
    "codes.web.devotions",
    "codes.web.disciplines",
    "codes.web.gifts",
    "codes.web.kiths",
    "codes.web.lodges",
    "codes.web.merits",
    "codes.web.orders",
    "codes.web.paths",
    "codes.web.powers",
    "codes.web.rites",
    "codes.web.scales",
    "codes.web.seemings",
    "codes.web.spells",
    "codes.web.spheres",
    "codes.web.theban",
    "codes.web.tribes"
]

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
