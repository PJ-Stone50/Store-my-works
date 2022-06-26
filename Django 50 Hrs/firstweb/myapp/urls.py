from django.urls import path, include
from .views import *





# ไฟล์นี้สร้างมาเพื่อ link กับ urls.py ที่อยู่ในโฟลเดอร์ firstweb (parents)

urlpatterns = [
    path('', Home, name='home-page'),	# Home คือฟังก์ชั่นที่อยู่ในไฟล์ views.py 
    
    path('about/', About, name='about-page'),
    path('contact/', Contact, name='contact-page'),
    path('product/', Product, name='product-page'),
    path('addproduct/', AddProduct, name='addproduct-page'),
    path('allproduct/', Product_stock, name='allproduct-page'),
    path('register/', Register, name='register-page'),
]

