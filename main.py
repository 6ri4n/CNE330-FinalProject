# CALCULATE AMOUNT OF USABLE IP ADDRESSES

# NOTE
# inputs: class type and subnet mask
# the following class types are supported: 'a' 'b' 'c'
# get_valid_subnet_mask() only checks if the octet is an integer and is a value between 0 and 255

def calculate_host_bits(host_octets):
    # TODO: perform calculation

    # calculate the host bits from host octet(s)
    host_bits = 0
    for octet_value in host_octets:
        decimal_bits = [128, 64, 32, 16, 8, 4, 2, 1]
        if octet_value == 0:
            host_bits += len(decimal_bits)
        else:
            while octet_value > 0:
                for decimal_value in decimal_bits[:]:
                    if octet_value >= decimal_value:
                        #print(str(octet_value) + " : " + str(decimal_value))
                        octet_value -= decimal_value
                        decimal_bits.remove(decimal_value)
            host_bits += len(decimal_bits)
            #print("done calculating - host bits: " + str(host_bits))
    # usable IPs = (2 ^ n) - 2
    return 2 ** host_bits - 2

def get_class_type():
    # TODO: input until a valid class type is given - returns the class type

    # check for valid class type - 'a' 'b' 'c'
    while True:
        class_type = input("\nEnter Class Type: ")
        if class_type.lower() == 'a':
            return 'a'
        elif class_type.lower() == 'b':
            return 'b'
        elif class_type.lower() == 'c':
            return 'c'
        else:
            print("Invalid Class Type, Please Try Again")

def get_host_octets(subnet_mask, class_type):
    # TODO: assign value to each octet

    #octet_one = int(subnet_mask.split('.')[0])
    octet_two = int(subnet_mask.split('.')[1])
    octet_three = int(subnet_mask.split('.')[2])
    octet_four = int(subnet_mask.split('.')[3])

    # set the host octets (dependent on the class type)
    if class_type == 'a':
        return [octet_two, octet_three, octet_four]
    elif class_type == 'b':
        return [octet_three, octet_four]
    elif class_type == 'c':
        return [octet_four]

def get_valid_subnet_mask():
    # TODO: ask for input until a valid subnet mask is given - returns the subnet mask

    # check for valid subnet mask
    user_input_state = False
    while not user_input_state:
        pass_counter = 0
        subnet_mask = input("Enter Subnet Mask: ")
        for octet in subnet_mask.split('.'):
            # valid octet is an integer and has a value between 0 and 255
            try:
                # checks each octet for an integer
                if isinstance(int(octet), int):
                    # checks each octet if value is within valid range
                    if int(octet) >= 0 and int(octet) <= 255:
                        # valid octet
                        pass_counter += 1
                    # not a valid octet
                    else:
                        break
                # not a valid octet
                else:
                    break
            # not a valid octet
            except Exception:
                break
        # each octet is valid = valid subnet mask
        if pass_counter == 4:
            user_input_state = True
        # invalid subnet mask - prompts user for another input
        else:
            print("Invalid Subnet Mask, Please Try Again")

    return subnet_mask

def num_of_usable_ips():
    # user input for class type
    class_type = get_class_type()

    # user input for subnet mask
    subnet_mask = get_valid_subnet_mask()

    # returns a list of host octets
    host_octets = get_host_octets(subnet_mask, class_type)

    # returns num of usable ips
    num_of_usable_ip_addresses = calculate_host_bits(host_octets)

    # TODO: return formatted string displaying amount of usable IPs from given subnet mask

    return "\nClass Type: " + class_type.upper() + "\nSubnet Mask: " + subnet_mask + "\nAmount of Usable IP Addresses: " + str(num_of_usable_ip_addresses) + "\n"

# TODO: ask if user wants to calculate again

user_input = input("Start (y/n): ")
# ask for input until a valid input is given
while user_input.lower() != 'y' and user_input.lower() != 'n':
    print("Invalid Response, Please Try Again")
    user_input = input("Start (y/n): ")

# continues calculating till user stops
while user_input.lower() == 'y':
    print(num_of_usable_ips())
    user_input = input("Again (y/n): ")