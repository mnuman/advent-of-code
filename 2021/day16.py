import utils

# set up simple dict to convert HEX digits to binary equivalents
hex_bin_digits = {f'{i:x}'.upper(): f'{i:0>4b}' for i in range(16)}


class Packet:
    def __init__(self, typeid, version, value=None, subpackets=None):
        self.typeid = typeid
        self.version = version
        self.value = value
        self.subpackets = [] if subpackets is None else subpackets

    def version_sum(self):
        return self.version + sum([p.version_sum() for p in self.subpackets])

    def packet_value(self):
        if self.value is  None:
            match self.typeid:
                case 0:                     # sum packet
                    self.value = sum([p.packet_value() for p in self.subpackets])
                case 1:
                    self.value = 1
                    for p in self.subpackets:
                        self.value *= p.packet_value()
                case 2:
                    self.value = min([p.packet_value() for p in self.subpackets])
                case 3:
                    self.value = max([p.packet_value() for p in self.subpackets])
                case 5:
                    self.value = 1 if self.subpackets[0].packet_value() > self.subpackets[1].packet_value() else 0
                case 6:
                    self.value = 1 if self.subpackets[0].packet_value() < self.subpackets[1].packet_value() else 0
                case 7:
                    self.value = 1 if self.subpackets[0].packet_value() == self.subpackets[1].packet_value() else 0
        return self.value


def readfile(filename):
    return utils.read_file(filename)


def hexadecimal_to_binary(hex_string):
    return ''.join([hex_bin_digits[c] for c in hex_string])


def consume_packet(binary_string):
    """
    Standard header:
    * 3 bits defining version (integer number)
    * 3 bits defining type
    """
    if len(binary_string) == 0:
        return

    packet_version = int(binary_string[:3], 2)
    packet_typeid = int(binary_string[3:6], 2)
    payload = binary_string[6:]  # pop off version & type

    match packet_typeid:
        case 4:  # literal packet
            done = False
            packet_result = ''
            while not done:
                packet_result += payload[1:5]
                done = payload[0] == '0'
                payload = payload[5:]                                           # pop off literal packet
            return Packet(packet_typeid, packet_version, value=int(packet_result, 2)), payload
        case _:  # operator packet
            if (payload[0]) == '0':
                subpacket_info, payload = int(payload[1:16], 2), payload[16:]   # number of bits in subpacket
                subpacket_string, payload = payload[:subpacket_info], payload[subpacket_info:]
                subpackets = []
                while subpacket_string:
                    subpacket, subpacket_string = consume_packet(subpacket_string)
                    subpackets.append(subpacket)
                return Packet(packet_typeid, packet_version, subpackets=subpackets), payload
            else:
                subpacket_info, payload = int(payload[1:12], 2), payload[12:]   # number of subpackets
                subpackets = []
                for i in range(subpacket_info):
                    subpacket, payload = consume_packet(payload)
                    subpackets.append(subpacket)
                return Packet(packet_typeid, packet_version, subpackets=subpackets), payload


def pop_off_padding_zeroes(original_length, current_payload):
    zeroes_to_discard = (4 - (original_length - len(current_payload)) % 4) % 4
    return current_payload[zeroes_to_discard:]  # pop off fillers zeroes to pad to multiple of 4


if __name__ == '__main__':
    hex_data = readfile("data/day-16.txt")
    bin_data = hexadecimal_to_binary(hex_data[0])
    result, remaining_payload = consume_packet(bin_data)
    part_1 = result.version_sum()
    print("Day 16 - part 1", part_1)
    part_2 = result.packet_value()
    print("Day 16 - part 2", part_2)
