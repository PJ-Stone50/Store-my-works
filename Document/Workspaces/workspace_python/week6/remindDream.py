def remindDream(n):
    fname = "Mr.A"
    lname = "ลืมความฝัน"
    if n <= 0 :
        return "เอาดีๆ เจ้าอย่าเพ้อเจ้อนัก ข้าปวดหัวกับเจ้าเสียเหลือเกิน"
    elif n < 5 :
        return (("ลูกผู้ชาย ใจนักเลงเว่ยยย !!!"+"\n")*n)
    return ((fname +" "+ lname+"ศักวันต้องได้ดี๊ !!!!!!!!" +"\n")*n)


n = int(input("จะทบทวนกี่ที : "))
print(remindDream(n))  
