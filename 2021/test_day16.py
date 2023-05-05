from day16 import *


def test_hexadecimal_to_binary():
    assert hexadecimal_to_binary('0') == '0000'
    assert hexadecimal_to_binary('D2FE28') == '110100101111111000101000'


def test_consume_literal_packet():
    result, remaining_payload = consume_packet('110100101111111000101000')
    assert result.version == 6, 'Version for literal packet is correct'
    assert result.typeid == 4, 'Package type for literal packet is correct'
    assert result.value == 2021, 'Literal value is correct'


def test_consume_fixed_subpackets():
    result, remaining_payload = consume_packet(hexadecimal_to_binary('EE00D40C823060'))
    assert result.version == 7, "Correct version for package with fixed number of sub-packages"
    assert result.typeid == 3, "Correct operator type for package with fixed number of sub-packages"
    assert len(result.subpackets) == 3, "Correct number of sub-packages"
    assert [p.typeid for p in result.subpackets] == [4, 4, 4], "Subpackets are all of type literal"
    assert [p.value for p in result.subpackets] == [1, 2, 3], "Subpackets have correct values"


def test_consume_length_subpackets():
    result, remaining_payload = consume_packet(hexadecimal_to_binary('38006F45291200'))
    assert result.version == 1, "Correct version for package with fixed length sub-packages"
    assert result.typeid == 6, "Correct operator type for package with fixed length sub-packages"
    assert len(result.subpackets) == 2, "Correct number of sub-packages"
    assert [p.typeid for p in result.subpackets] == [4, 4], "Subpackets are all of type literal"
    assert [p.value for p in result.subpackets] == [10, 20], "Subpackets have correct values"


def test_packet_version_sum():
    result, remaining_payload = consume_packet(hexadecimal_to_binary('8A004A801A8002F478'))
    assert result.version_sum() == 16
    result, remaining_payload = consume_packet(hexadecimal_to_binary('620080001611562C8802118E34'))
    assert result.version_sum() == 12
    result, remaining_payload = consume_packet(hexadecimal_to_binary('C0015000016115A2E0802F182340'))
    assert result.version_sum() == 23
    result, remaining_payload = consume_packet(hexadecimal_to_binary('A0016C880162017C3686B18A3D4780'))
    assert result.version_sum() == 31


def test_packet_value():
    result, remaining_payload = consume_packet(hexadecimal_to_binary('C200B40A82'))
    assert result.packet_value() == 3
    result, remaining_payload = consume_packet(hexadecimal_to_binary('04005AC33890'))
    assert result.packet_value() == 54
    result, remaining_payload = consume_packet(hexadecimal_to_binary('880086C3E88112'))
    assert result.packet_value() == 7
    result, remaining_payload = consume_packet(hexadecimal_to_binary('CE00C43D881120'))
    assert result.packet_value() == 9
    result, remaining_payload = consume_packet(hexadecimal_to_binary('D8005AC2A8F0'))
    assert result.packet_value() == 1
    result, remaining_payload = consume_packet(hexadecimal_to_binary('F600BC2D8F'))
    assert result.packet_value() == 0
    result, remaining_payload = consume_packet(hexadecimal_to_binary('9C005AC2F8F0'))
    assert result.packet_value() == 0
    result, remaining_payload = consume_packet(hexadecimal_to_binary('9C0141080250320F1802104A08'))
    assert result.packet_value() == 1
