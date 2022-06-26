class Student:

  def __init__(self,name,age,gender=None):
    self.name = name
    self.age = age
    self.gender = gender
    if self.gender == None:
      print('! ผู้ใช้ลืมกรอก gender')

  def study(self):
    print(f'{self.name}กำลังเรียนอยู่')

  def sawatdee(self):
    if self.gender == 'ชาย':
      tail = 'ครับ'
      callme = 'ผม'
    else:
      tail = 'ค่ะ'
      callme = 'หนู'

    print(f'สวัสดี{tail} {callme}ชื่อ{self.name}')


# Inheritance from class Student
class SpecialStudent(Student):

  def __init__(self,name,age,gender,parent):
    super().__init__(name,age,gender)
    self.parent = parent


  def hello(self, person='เพื่อน'):
    if person == 'เพื่อน':
      print('ว่าไง..')
    else:
      print('เปิดฟังก์ชันตาบอด')

  def sawatdee(self):
    print(f'หวัดดี ชื่อ{self.name}')

  def myfather(self):
    print('รู้ไหมผมลูกใคร ?')
    print(f'ผมลูก{self.parent}')


class Teacher:

  def __init__(self,name,gender,subject):
    self.name = name
    self.gender = gender
    self.subject = subject

  def teach(self):
    print('คุณครู{}กำลังสอนวิชา{}'.format(self.name,self.subject))


if __name__ == '__main__':
  student1 = Student('สมชาย', 14, 'ชาย')
  student2 = Student('สมศรี', 14, 'หญิง')
  special_student = SpecialStudent('จ้อย', 16, 'ชาย','ลูกนายกอบต เจต')

  teacher1 = Teacher('จอน','ชาย','ภาษาอังกฤษ')
  print(teacher1.name)
  print(teacher1.subject)

  