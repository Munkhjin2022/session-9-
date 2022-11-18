total = 0.0
t = 0.0

def comptotal(q, up):
  global total
  total = q * up
  global t
  t = round(total * 0.07, 2)

print("total ", total)
q = float(input("The enter quantity "))
up = float(input("The enter unit price "))

comptotal(q, up)

print("The total ", total)
print("The tax ", t)