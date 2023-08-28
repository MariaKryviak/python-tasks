"""
Must be 17 characters long.
Must have colons between octets.
Hex letters must be uppercase.
Valid example
"DE:F0:FE:DC:B8:76"
"FF:FF:FF:FF:FF:FF"
"""


def validate_mac_address(mac: str) -> bool:
    every_third_value = mac[2::3]
    if len(mac) == 17 and all(char in ":" for char in every_third_value):
        for char in mac:
            if not char.isdigit() and char.islower():
                return False
        return True
    else:
        return False


assert False == validate_mac_address("")
assert False == validate_mac_address("0")
assert False == validate_mac_address("00")
assert False == validate_mac_address("00:")
assert False == validate_mac_address("00:0")
assert False == validate_mac_address("00:00")
assert False == validate_mac_address("00:00:")
assert False == validate_mac_address("00:00:0")
assert False == validate_mac_address("00:00:00")
assert False == validate_mac_address("00:00:00:")
assert False == validate_mac_address("00:00:00:0")
assert False == validate_mac_address("00:00:00:00")
assert False == validate_mac_address("00:00:00:00:")
assert False == validate_mac_address("00:00:00:00:0")
assert False == validate_mac_address("00:00:00:00:00")
assert False == validate_mac_address("00:00:00:00:00:")
assert False == validate_mac_address("00:00:00:00:00:0")

assert False is validate_mac_address("00x00:00:00:00:00")
assert False is validate_mac_address("00:00.00:00:00:00")
assert False is validate_mac_address("00:00:00-00:00:00")
assert False is validate_mac_address("00:00:00:00900:00")
assert False is validate_mac_address("00:00:00:00:00?00")

assert False is validate_mac_address("a0:00:00:00:00:00")
assert False is validate_mac_address("0b:00:00:00:00:00")
assert False is validate_mac_address("00:c0:00:00:00:00")
assert False is validate_mac_address("00:0d:00:00:00:00")
assert False is validate_mac_address("00:00:e0:00:00:00")
assert False is validate_mac_address("00:00:0f:00:00:00")

assert True is validate_mac_address("00:00:00:00:00:00")
assert True is validate_mac_address("12:34:56:78:9A:BC")
assert True is validate_mac_address("DE:F0:FE:DC:B8:76")

print("Done")
