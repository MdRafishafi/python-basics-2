# conditional logic
is_old = False
is_licenced = True

# 1. if else condition
if is_old:
  print("you can drive!")
else:
  print("you cannot drive!")

# 2. if else if condition
if is_old:
  print("you can drive!")
elif is_licenced:
  print('you can drive because you have a licenc')
else:
  print("you cannot drive!")

# 3. Ternary Opration
# true_value if condition else false_value
print('value is true') if True else print('value is false')