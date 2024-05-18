import string
import random

def convertStringToInteger(user_input, field_name):
  if user_input.isdigit():
    return int(user_input)
  else:
    print(f'Try to enter a number the next time in field {field_name}.')
    return 0
  
def validateError(nb_characters, nb_digits, nb_special_caracters):
  nb_total_other_characters = nb_digits + nb_special_caracters
  if nb_total_other_characters > nb_characters:
    print('The sum of the number of digits and the numbers of special characters entered are higher than the number of total characters. You will only get letters.\r\n')
    return True
  
  return False
  
def getUserInput(question, field_name):
  nb_characters_input = input(f'{question}\r\n')
  return convertStringToInteger(nb_characters_input, field_name)

def getListOfIndex(nb_other_characters, index_list):
  list_of_index = []
  for i in range(nb_other_characters):
    digit = random.choice(index_list)
    list_of_index.append(digit)
    index_list.remove(digit)

  return list_of_index

def showPassword(password):
  print('\r\n')
  print('---------------------------------\r\n')
  print(f"Your password: {password}")

def generatePassword(nb_characters, digit_index_list, special_characters_index_list, i, password):
  if i in digit_index_list: password += random.choice(string.digits)
  elif i in special_characters_index_list: password += random.choice(string.punctuation)
  else: password += random.choice(string.ascii_letters)

  if nb_characters >= len(password):
    i += 1
    generatePassword(nb_characters, digit_index_list, special_characters_index_list, i, password)
  else: showPassword(password)

def main():
  print('Générer son mot de passe complexe\r\n')
  print('---------------------------------\r\n')
  nb_characters = getUserInput('How many characters do you need in your your password?', 'number of characters in password')
  nb_digits = getUserInput('How many digits?', 'number of digits')
  nb_special_caracters = getUserInput('How many special characters?', 'number of special characters')
  index_list = list(range(0, nb_characters))
  
  if validateError(nb_characters, nb_digits, nb_special_caracters):
    nb_digits = 0
    nb_special_caracters = 0

  digit_index_list = []
  if nb_digits > 0:
    digit_index_list = getListOfIndex(nb_digits, index_list)

  special_characters_index_list = []
  if nb_special_caracters > 0:
    special_characters_index_list = getListOfIndex(nb_special_caracters, index_list)

  generatePassword(nb_characters, digit_index_list, special_characters_index_list, 0, '')

main()