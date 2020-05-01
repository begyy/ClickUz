#Ishni boshlash
O'rtanib olganimizdan song settins.py ga o'rnatilgan packageni qo'shib qoyish kerak
```python
INSTALLED_APPS = [
    'clickuz',
    'rest_framework'
]
```
undan song quydagi komandani bajarishmiza kerak yani bazani migrate qib olish kerak
```
python manage.py migrate
```
# Buyurtmani tekshirsh
Buyurtmani tekshirishda sizga buyurtmani raqami va narxi keladi uni siz bazadan tekshirishingiz
xaqatan buyurtma mavjudmi yoki yoq va narxi bir biriga tori kelishini.
```
1. Agar buyurtma bolib narxi narxiga tori kelsa return self.ORDER_FOUND
2. Agar buyurtma bolib turib narxi bir biriga tog'ri kelmasa return self.INVALID_AMOUNT
3. Agar buyurtma yoq bolsa return self.ORDER_NOT_FOUND
```
Misol uchun mana example.py
```python
from clickuz import ClickUz

class CheckOrderAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        return self.ORDER_FOUND # self.ORDER_NOT_FOUND # self.INVALID_AMOUNT

    def successfully_payment(self, order_id: str, transaction: object):
        print(order_id)
        print(transaction)
```