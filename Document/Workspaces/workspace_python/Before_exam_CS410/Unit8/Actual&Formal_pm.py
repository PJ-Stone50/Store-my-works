def Defination(name,price):
  result = ('%s'%name +' %.2f'%price)
  print(result)

Defination('A',100)
#แก้ด้วยการ assign ด้วยชื่อ keyword arguement ให้มันตรงกับ datatype
Defination(price=100,name='A')

#ขอแค่ Datatpye ตรงกับ key ที่ใส่ใน arg แล้วมีจำนวน element เท่ากัน ระหว่าง Actual กับ Formal