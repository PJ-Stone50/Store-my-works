Stringset = input("Enter Student Id : ")
Set = Stringset
print(sorted(set(Set)))

n = ("n = %d"%len(Set))
print(n)
sub1 = []

for data in Set:
  if '1' in data:
    