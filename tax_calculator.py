# A = P(1 + r/n)^nt
# A = P(1 + rt)

interest_type = input('Interest Type (Compound or Simple): ').lower()

while interest_type != 'compound' and interest_type != 'simple':
  print('Error: Invalid interest type. Please enter either "compound" or "simple".')
  interest_type = input('Interest Type (Compound or Simple): ').lower()

amount = input('Amount: ')
rate = input('Rate: ')
time = input('No. of years: ')


def calculator(interest_type, amount, rate, time):
  if interest_type == 'compound':
    return amount * (1+ rate)**(time)
  elif interest_type == 'simple':
    return amount * (1+ rate*time)
  

print(calculator(interest_type, amount, rate, time))
