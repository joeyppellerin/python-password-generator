import random

password = 'FDSewr$/%$%2309'
password_list = list(password)
print(random.shuffle(list(password_list)))
print(''.join(password_list))
