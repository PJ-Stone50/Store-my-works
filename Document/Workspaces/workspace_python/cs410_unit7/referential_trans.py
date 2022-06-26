count = int(input("Enter count of Square : "))

def Cal(val1,val2):
  area = val1 * val2
  return area

width = int(input("Enter width : "))
height = int(input("Enter height : "))

result1 = (count * Cal(width,height))
area = Cal(width,height)
result2 = (count * area)

print('ผลรวมพื้นที่สี่เหลี่ยมจำนวน %d อัน เท่ากับ'%count,result1)
print('ผลรวมพื้นที่สี่เหลี่ยมจำนวน %d อัน เท่ากับ'%count,result2)
