def compavg(sc1, sc2, sc3):
  avg = (sc1 +sc2 + sc3)/3
  h= (200-avg)*0.9
  avghand=((sc1+h)+(sc2+h)+(sc3+h))/3

  return avg, avghand

name = input("Enter the last name ")
sc1 = float(input("Enter the first game score"))
sc2 =float(input("Enter the second game score"))
sc3 = float(input("Enter the third game score"))

avg, avghandi = compavg(sc1, sc2, sc3)

print("The last name: ", name)
print("The average score: ", avg)
print("The average score with handicap: ", avghandi)