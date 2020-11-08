# example for arguments (*arg) and keyword_argments (**kwarg)
# arg creates an tuple with arguments
# kwarg creates an dictionary with named arguments
def numbers(*arg,**kwarg):
  print(f'arg -> {arg}')
  print(f'kwarg -> {kwarg}')