def compt(q,p,r):
  total=float(q)*float(p)
  discount=float(total)*float(r)
  disprice=total-discount

  return discount, disprice

q=float(input("Enter the quantity "))
p=float(input("Enter the price"))
r=float(input("Enter the discount rate "))

discount, disprice=compt(q,p,r)

print("The quantity: ", q)
print("The price: ", p)
print("The discount amount: ", discount)
print("The discounted price: ", disprice)

