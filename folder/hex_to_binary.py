
def hex_to_binary(hex_num):
  hex_num = hex_num.upper()
  hex_to_binary_dict = {
      '0': '0000',
      '1': '0001',
      '2': '0010',
      '3': '0011',
      '4': '0100',
      '5': '0101',
      '6': '0110',
      '7': '0111',
      '8': '1000',
      '9': '1001',
      'A': '1010',
      'B': '1011',
      'C': '1100',
      'D': '1101',
      'E': '1110',
      'F': '1111'
  }
  binary_num = ""
  for digit in hex_num:
    if digit not in hex_to_binary_dict:
      return "ERROR"
    binary_num += hex_to_binary_dict[digit]
  return binary_num

# Example usage
hex_number = "12DCEE"
binary_equivalent = hex_to_binary(hex_number)
print(f"{hex_number} in binary is: {binary_equivalent}")