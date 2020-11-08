# looping statements
# iterable - list, dictionary, tuple, set, string.
def loop():
  # 1. for loop
  print('\n---------for loop exampal---------')
  for item in 'Banglore':
    print(item)
  
  # 2. for loop with the dictionary
  user = {
    'place': 'Banglore',
    'area': 1000,
  }
  print("\nfor loop with the dictionary")
  for user_data in user:
    print(user_data)
  print("\nfor loop with the dictionary with items")
  for user_data in user.items():
    print(user_data)
  print("\nfor loop with the dictionary with items and tuple unpacking")
  for key,value in user.items():
    print(key , value)
  print("\nfor loop with the dictionary with keys")
  for user_data in user.keys():
    print(user_data)
  print("\nfor loop with the dictionary with values")
  for user_data in user.values():
    print(user_data)
  print("\nfor loop with the enumerate")
  for index,value in enumerate('Hello'):
    print(index,value)
  print("\nwhile loop with the enumerate")
  i = 0
  while i < 5:
    print(i)
    i += 1
  else:
    print('While is done')
