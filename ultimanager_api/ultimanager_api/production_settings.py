"""
Settings used in production.
"""

from ultimanager_api.settings import *      # noqa


ALLOWED_HOSTS = [
    '.api.ultimanager.com',
    'localhost',
]

DEBUG = False


# Use the local settings created by Ansible if they exist

try:
    from ultimanager_api.local_settings import *    # noqa
except ImportError:
    pass
