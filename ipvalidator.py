import re
from enum import Enum


class IPType(Enum):
    ipv4 = {'id': 1, 'name': 'ipv4'}
    ipv6 = {'id': 2, 'name': 'ipv6'}


def ipv4_validator(ip: str) -> bool:
    pat = r'^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}'
    ipv4_rx = re.compile(pat)
    return bool(ipv4_rx.match(ip))


def ipv6_validator_new(ip: str) -> bool:
    pat = r'(([A-F0-9]{1,4})(:(?!$)|$)){8}'
    ipv6_rx = re.compile(pat, re.IGNORECASE)
    return bool(ipv6_rx.match(ip))


def ipv6_validator(ip: str) -> bool:
    pat = r'([A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$'
    ipv6_rx = re.compile(pat)
    return bool(ipv6_rx.match(ip.upper()))


def ip_check(ip: str) -> (int, str):
    iptype_id, name = -1, 'Neither'

    if ipv4_validator(ip):
        iptype_id, name = IPType.ipv4.value['id'], IPType.ipv4.value['name']

    if ipv6_validator(ip):
        iptype_id, name = IPType.ipv6.value['id'], IPType.ipv6.value['name']

    return iptype_id, name
