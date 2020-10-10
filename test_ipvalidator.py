from ipvalidator import ip_check


iplist = [
    ("172.16.254.1", (1, "ipv4")),
    ("256.256.256.256", (-1, "Neither")),
    ("172.16.254.01", (-1, "Neither")),
    ('2001:db8:85a3:0:0:8A2E:0370:7334', (2, 'ipv6')),
    ('2001:0db8:85a3:0000:0000:8a2e:0370:7334', (2, 'ipv6')),
    ('2001:0db8:85a3::8A2E:0370:7334', (-1, "Neither")),
    ('02001:0db8:85a3:0000:0000:8a2e:0370:7334', (-1, "Neither")),
]


def test_validator():
    for ip, ans in iplist:
        assert ip_check(ip) == ans
