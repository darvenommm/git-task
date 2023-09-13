from functools import reduce


def binary_to_decimal(binary_number: str) -> int:
    return int(binary_number, 2)


def get_char_by_binary_number(binary_number: str) -> str:
    return chr(binary_to_decimal(binary_number))


chars = [
    '1001000', '1100001', '1110000', '1110000', '1111001',
    '1000000', '1110000', '1110010', '1101111', '1100111',
    '1110010', '1100001', '1101101', '1101101', '1110010',
    '1110011', '1000000', '1100001', '1111001', '1000001',
]


def reduce_chars(result: str, char: str) -> str:
    return result + get_char_by_binary_number(char)


print(reduce(reduce_chars, chars, ''))
