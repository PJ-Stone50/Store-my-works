from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse	# HttpResponse เป็นฟังก์ชันสำหรับโชว์ข้อความหน้าเว็บได้
from .models import Allproduct, Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.



def Home(request):
	product = Allproduct.objects.all().order_by('id').reverse()[:3] # ดึงข้อมูลมาทั้งหมด..?  คำสั่งนี้ใช้สลับตำแหน่งหัว-ท้าย เวลาสินค้าหมด".order_by('id').reverse()"
	preorder = Allproduct.objects.filter(quantity__lte=0)
	#quantity__lte=0 (หาค่าที่ quantity <= 0 - lte is <=)
	#quantity__gt
	context = {'product':product,'preorder':preorder}
	return render(request, 'myapp/home.html',context) # สั่งให้หน้าเว็บ local:8000 เป็นไปตามไฟล์ที่ชื่อ home.html ที่อยู่ในโฟลเดอร์ชื่อ myapp

def Home2(request):
	
	return render(request, 'myapp/home2.html') # สั่งให้หน้าเว็บ local:8000 เป็นไปตามไฟล์ที่ชื่อ home.html ที่อยู่ในโฟลเดอร์ชื่อ myapp

def Google(request):
	return render(request, 'myapp/google_test.html')

def About(request):
	return render(request, 'myapp/about.html')


def Contact(request): # ทำไงให้เวลากด submit หน้า contact.html แล้วให้เก็บข้อมูลลงฟังก์ชันนี้ OMG, ถ้ามีเนื้อดูดรับรอง ปัญหานี้ต้องถูกแก้ไข Oh shit ขี้จนหมดไส้แล้วเนื้อยังไม่มาเล้ยยยยยยย
	return render(request, 'myapp/contact.html')

def AddProduct(request): #โอ้มายก้อด ต้องรื้อความจำใหม่หมดเลยหร้ออออออออออออ
	# หากเจ้านั่นไม่ใช่ admin จงถอยกลับไป home-page บัดเดี๋ยวนี้ !!! หมายถึงมีคนลักไก่เข้า addproduct แต่ไม่ใช่แอดมิน โดยการเข้า website ด้วย url (http://localhost:8000/addproduct/)
	if request.user.profile.usertype != 'admin' :
		return redirect('home-page') # redirect คือคำสั่ง วาร์ป...



	if request.method == 'POST' and request.FILES['imageupload']:
		data = request.POST.copy() # ดึงข้อมูลจากหน้า html(addproduct-page)
		name = data.get('name') # ดึงข้อมูลจากหน้า html(addproduct-page) => name = "name"
		price = data.get('price') # ดึงข้อมูลจากหน้า html(addproduct-page) => name = "price"
		detail = data.get('detail') # ดึงข้อมูลจากหน้า html(addproduct-page) => name = "detail"
		imageurl = data.get('imageurl') # ดึงข้อมูลจากหน้า html(addproduct-page) => name = "imageurl"
		quantity = data.get('quantity')
		unit = data.get('unit')
		

		new = Allproduct()
		new.name = name
		new.price = price
		new.detail = detail
		new.imageurl = imageurl
		new.quantity = quantity
		new.unit = unit

		###################SAVE IMAGE########################
		file_image = request.FILES['imageupload']
		file_image_name = request.FILES['imageupload'].name.replace(' ','')
		print('### upload FILE_IMAGE:',file_image)
		print('### upload IMAGE_NAME:',file_image_name)
		fs = FileSystemStorage()
		filename = fs.save(file_image_name,file_image)
		upload_file_url = fs.url(filename)
		new.image = upload_file_url[6:]
		#####################################################
		new.save()
	return render(request, 'myapp/addproduct.html')

def Product(request):
	item1 = 'Apple juice'
	item2 = 'Grape juice'
	item3 = 'Orange juice'
	item4 = 'Carrot juice'
	item5 = 'Cranberry juice'
	item6 = 'Coconut juice'
	item7 = 'Cucumber juice'
	item8 = 'Lemon juice'
	item9 = 'Mango juice'
	item10 = 'Papaya juice'
	item11 = 'Guava juice'
	item12 = 'Melon juice'
	# items = ['Apple', 'Grape', 'Almond', 'Avocado']
	# number = 0
	# for item in items:
	#     number += 1
	#     print(number, item)

	# img1 = PhotoImage(file='images/django.png').subsample(2,2)

	context = {'item1':item1,'item2':item2,'item3':item3,'item4':item4,'item5':item5,'item6':item6,'item7':item7,'item8':item8,'item9':item9,'item10':item10,'item11':item11,'item12':item12}
	return render(request, 'myapp/product.html',context)


def Product_stock(request):
	product = Allproduct.objects.all().order_by('id') # ดึงข้อมูลมาทั้งหมด..?  คำสั่งนี้ใช้สลับตำแหน่งหัว-ท้าย เวลาสินค้าหมด".order_by('id').reverse()"

	context = {'product':product}
	return render(request, 'myapp/allproduct.html',context)




def Register(request):
	if request.method == 'POST':
		data = request.POST.copy() 
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email') 
		password = data.get('password')
		# ยังไม่ใส่ try except เพื่อป้องกันการสมัครซ้ำ
		# +alert ว่าอีเมล์นี้เคยสมัครแล้ว
		#
		newuser = User() # Create new user
		newuser.username = email
		newuser.email = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.set_password(password) # Set password 
		newuser.save()

		profile = Profile() # Reference profile with Function name's Profile from model.s that I imported on the top of page.
		profile.user = User.objects.get(username=email) # Do it as same as upper line.
		profile.save() # อย่าลืมเซฟนะเด็กดีๆ

		user = authenticate(username=email, password=password) # Auto-login เวลา user สมัครสมาชิคเสร็จจะ login autoโนมัติ์
		login(request,user) # แต่ยังไม่เด้งเข้าหน้า home-page [ยังคงคา] อยู่ที่ register-page

	return render(request, 'myapp/register.html')