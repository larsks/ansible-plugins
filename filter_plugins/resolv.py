# (c) 2014, Maciej Delmanowski <drybjed@gmail.com>
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

import socket

from ansible import errors


def _resolv(v):
    try:
        r = socket.gethostbyname_ex(v)
    except socket.gaierror as exc:
        raise errors.AnsibleFilterError(
            'failed to resolv hostname "%s": %s' % (v, exc))
    else:
        return r


def filter_resolv(v):
    r = _resolv(v)
    return r[2][0]


def filter_resolv_all(v):
    r = _resolv(v)
    return r[2]


class FilterModule(object):
    ''' Hostname lookup filter '''
    filter_map =  {
        'resolv': filter_resolv,
        'resolv_all': filter_resolv_all,
    }

    def filters(self):
        return self.filter_map
