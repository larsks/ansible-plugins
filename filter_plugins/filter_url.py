# (c) 2015 Ansible Project Contributors
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible import errors
from ansible.compat.six.moves import urllib


def filter_netloc(v):
    '''parses the "authority" component of a URL to extract a username,
    password, and hostname'''
    hostname = v
    username = None
    password = None

    try:
        creds, hostname = v.split('@')
        try:
            username, password = creds.split(':', 1)
        except ValueError:
            raise errors.AnsibleFilterError(
                'failed to parse credentials from netloc')
    except ValueError:
        pass

    return {
        'username': username,
        'password': password,
        'hostname': hostname,
    }

class FilterModule(object):
    '''Provides URL splitting filters'''
    filter_map = {
        'urlparse': urllib.parse.urlsplit,
        'urlsplit': urllib.parse.urlsplit,
        'urldefrag': urllib.parse.urldefrag,
        'urlcreds': filter_netloc,
    }

    def filters(self):
        return self.filter_map
