def compavg(ex1, ex2, ex3):
  t = ex1 + ex2 + ex3
  avg= round(t/3, 2)

  return t, avg

name = input("Enter the last name")
ex1 = float(input("Enter the first exam score"))
ex2 =float(input("Enter the second exam score"))
ex3 = float(input("Enter the third exam score"))

t, avg = compavg(ex1, ex2, ex3)

print("The last name: ", name)
print("The total points: ", t)
print("The average exam score: ", avg)