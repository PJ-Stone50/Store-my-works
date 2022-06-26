def Cal(val):
  val += 4
  return (3 * val - 1)


i,j = 10,10
sum1 = (i/2) + (Cal(j))
sum2 = (Cal(j)) + (j/2)

print("Sum1 : %d"%sum1)
print("Sum2 : %d"%sum2)

