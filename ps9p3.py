def compcommis(sales):
  if sales>100000:
    c=0.1
  else:
    c=0.05

  target=sales*0.05

  return c, target

name = input("Enter the last name")
sales = float(input("Enter the sales"))


c, target = compcommis(sales)

print("The last name: ", name)
print("The commission: ", c)
print("The next year's target: ", target)