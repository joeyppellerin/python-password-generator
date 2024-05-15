import string
import random

def convertStringToInteger(user_input, field):
  if user_input.isdigit():
    return int(user_input)
  else:
    print(f'Try to enter a number the next time in field {field}.')
    return 0

nb_characters = 0
nb_special_characters = 0
nb_digits = 0

print('Générer son mot de passe complexe\r\n')
print('---------------------------------\r\n')
nb_characters_input = input('How many characters do you need in your your password?\r\n')
nb_characters = convertStringToInteger(nb_characters_input, 'number of characters in password')

nb_digits_input = input('How many digits?\r\n')
nb_digits = convertStringToInteger(nb_digits_input, 'number of digits')

nb_special_caracters_input = input('How many special characters?\r\n')
nb_special_caracters = convertStringToInteger(nb_special_caracters_input, 'number of special characters')

digit_index_list = []
for i in range(nb_digits):
  digit_index_list.append(random.sample(list(range(0, nb_characters))))

special_characters_index_list = []
for i in range(nb_special_caracters):
  print(i)
  special_characters_index_list.append(random.sample(list(range(0, nb_characters))))

print(digit_index_list)
print(special_characters_index_list)

password = ''
for i in range(nb_characters):
  if i in digit_index_list:
    password += random.choice(string.digits)
  elif i in special_characters_index_list:
    password += random.choice(string.punctuation)
  else:
    password += random.choice(string.ascii_letters)


print('\r\n')
print('---------------------------------\r\n')
print(f'Your password: {password}')

