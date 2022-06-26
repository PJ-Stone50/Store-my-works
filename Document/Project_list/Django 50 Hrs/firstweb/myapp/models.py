# ||คือถ้าอยากเพิ่มอะไรในหน้า admin/User ให้มาแก้ที่หน้านี้ zZZ
from django.db import models
# || ใช้สำหรับฟังก์ชัน Profile
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="photoprofile",null=True,blank=True,default='default.png')
	usertype = models.CharField(max_length=100,default='member')

	def _str_(self):
		return self.user.first_name



class Allproduct(models.Model): # ฟังก์ชันในหน้าแก้ไขสินค้าใน admin-page

	name = models.CharField(max_length = 100)
	price = models.CharField(max_length = 100)
	detail = models.TextField(null = True,blank = True)
	imageurl = models.CharField(max_length=200,null = True,blank = True)
	instock = models.BooleanField(default=True)
	quantity = models.IntegerField(default=1)
	unit = models.CharField(max_length=200,default='')
	image = models.ImageField(upload_to="imageproduct",null=True,blank=True)

	# อย่าลืมทำปุ่ม Delete สำหรับลบหลายๆออเดอร์ในครั้งเดียวนะครับ

	def __str__(self):
		print("Check Product Now.")
		return self.name