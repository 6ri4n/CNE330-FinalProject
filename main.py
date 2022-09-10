# This program returns the count of IPs within a range that would be allocated to different OSes
def linux_mac_windows(starting_ip, ending_ip):
    '''Returns the count of IPs within a range that would be allocated to different OSes'''
    assert starting_ip.findall('.') == 3, f"starting ip addresses require 4 octets"
    assert ending_ip.findall('.') == 3, f"ending ip addresses require 4 octets"

    linux_count = 0  # Numbers divisible by 3
    mac_count = 0  # Numbers divisible by 5
    windows_count = 0  # Numbers divisible by 3 and 5

    start = list(starting_ip.split('.'))
    end = list(ending_ip.split('.'))
    assert start[3] >= 0, f"starting ip address should be valid"
    assert start[3] <= 256, f"starting ip address should be valid"
    assert end[3] >= 0, f"ending ip address should be valid"
    assert end[3] <= 256, f"ending ip address should be valid"
    start_count = int(start[3])
    end_count = int(end[3])
    for i in range(start_count, end_count + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                windows_count += 1
        else:
            linux_count += 1
        if i % 5 == 0:
            if i % 3 == 0:
                windows_count += 1
        else:
            mac_count += 1

    return linux_count, mac_count, windows_count
