def Cal(val1,val2):
  area = val1 * val2
  return area

count = int(input("ระบบจำนวนสี่เหลี่ยม : "))
result1 = (count * Cal(2,3))
area = Cal(2,3)
result2 = (count * area)

print('ผลรวมพื้นที่สี่เหลี่ยมจำนวน %d อัน เท่ากับ'%count,result1)
print('ผลรวมพื้นที่สี่เหลี่ยมจำนวน %d อัน เท่ากับ'%count,result2)
