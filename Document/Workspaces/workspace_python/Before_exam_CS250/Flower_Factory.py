# Polymorphism
class LST25:

    
    def __init__(self,name,price):
      self.name = name
      self.price = price

      if (self.name is None):
        self.name = "Unknow Species"
      elif (self.price is None):
        self.price = "Undefined"

    # Expense Per Day
    def lightning(self,hour):
      global price_lightning_hour, budget

      # ค่าแสงสว่างหลอดไฟชั่วโมงละ 2 บาท
      price_lightning_hour = hour * 2
      budget -= price_lightning_hour
      print("ค่าไฟสำหรับปลูกต้นไม้ %d"%price_lightning_hour)
      print("คุณเหลือยอดเงิน %d บาท"%budget)
      return budget


    def watering(self,round):
      global water_capacity,price_watering,budget
      # รดน้ำรอบละ 2 แกลลอน
      water_use = (round * 2)
      water_capacity -= water_use

      # ค่าน้ำแกลลอนละ 10 บาท
      price_watering = (water_use * 10) 
      budget -= price_watering

      print("เหลือน้ำบรรจุในสระ %d แกลลอน"%water_capacity)
      print("ค่าน้ำสำหรับปลูกต้นไม้ %d บาท"%price_watering)
      print("คุณเหลือยอดเงิน %d บาท"%budget)    
      return water_capacity, budget


    def calculateExpense_month(self,month):
      global sumEx
      month *= 30
      formula =  price_lightning_hour + price_watering 
      sumEx = month * formula
      print("*รายเดือน* ค่าใช้จ่ายสำหรับปลูกต้นไม้ทั้งเดือนเท่ากับ %d"%sumEx)
      print("ยอดคงเหลือของท่าน",budget - sumEx)
      return sumEx

      

    def addInfo(self,name,price):
      self.name = name
      self.price = price

กำไร = (จน.ผลผลิต * ราคาขาย) - ต้นทุน
กำไร(รายเดือน) = (จน.ผลผลิต(รายเดือน) * ราคาขาย) - ต้นทุน
พอก่อนฮ่าๆ เดี๋ยวพรุ่งนี้ไม่ไหว

class BlueGorilla:
  
    def __init__(self,name,price):
      self.name = name
      self.price = price

      if (self.name is None):
        self.name = "Unknow Species"
      elif (self.price is None):
        self.price = "Undefined"


    def watering(self,round):
      global water_capacity
      water_capacity -= (round * 150)
      print("%d gallon remaining in the pool"%water_capacity)
      return water_capacity
      

    def addInfo(self,name,price):
      self.name = name
      self.price = price
     



# Maximum water_capacity is 1000 gallon 
water_capacity = 200
budget = 10000
price_lightning_hour = 1
sumEx = 0

lst = LST25("เมากระจาย",2500)
lst.watering(2)
lst.lightning(16)
# lst.sumEx(2)
lst.calculateExpense_month(1)

# blue_gorilla = BlueGorilla("แดดแยงตา", 3600)
# blue_gorilla.watering(2)


