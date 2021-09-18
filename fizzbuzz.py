#########################(important)###############################
for numbers in range(0,101):
  if numbers%5==0 and numbers%3==0:
    print('Fizzbuzz')
  elif numbers%3==0:
    print('buzz')
  elif numbers%5==0:
    print('Fizz')
  print(numbers)      