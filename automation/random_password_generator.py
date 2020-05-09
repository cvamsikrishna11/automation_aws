from random import choice

len_of_password = 8
valid_chars_for_password = 'abcdefghijklmnopqrstuvwxyz1234!@#$'

print(choice(valid_chars_for_password))

password = []
for each_char in range(len_of_password):
    password.append(choice(valid_chars_for_password))

rand_pass = ''.join(password)
print(rand_pass)

# in a single line
rand_pass1 = ''.join(choice(valid_chars_for_password) for each_char in range(len_of_password))
print(rand_pass1)
