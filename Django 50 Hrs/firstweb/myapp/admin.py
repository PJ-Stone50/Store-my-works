from django.contrib import admin
from .models import Allproduct, Profile # ดึง Allproduct มาจากไฟล์ชื่อ models.py

# Register your models here.
# คำสั่ง below คือฟังก์ชันในหน้า admin ที่อยู่ในตาราง myapp
admin.site.register(Allproduct)
admin.site.register(Profile)