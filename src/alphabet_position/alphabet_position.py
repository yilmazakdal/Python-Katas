def alphabet_position(string):
  alphabet_position = ''
  lower_case = string.lower()
  for letter in  lower_case:
    if letter.isalpha():
      letter_value = str(ord(letter) - 96)
      alphabet_position += letter_value + ' '
  return alphabet_position[:-1]