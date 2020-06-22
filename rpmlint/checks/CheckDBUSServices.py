from .Allowlisting import AbstractSimpleAllowlistCheck


class DBUSServiceCheck(AbstractSimpleAllowlistCheck):
    """ Verifies that installed D-Bus services are on an allow list. """
    restricted_paths = (
        '/usr/share/dbus-1/system-services/',
        '/usr/share/dbus-1/system.d/',
        '/etc/dbus-1/system.d/'
    )
    error_map = {
        'ghost': 'suse-dbus-ghost-service',
        'unauthorized': 'suse-dbus-unauthorized-service',
    }
    allowlist_config_key = 'DBUSServices.WhiteList'
