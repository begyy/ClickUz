#Buyurtmani tekshirsh

Bizaga kelgan buyurtmani tekshirishimza kerak **ClickUz** klassini davom etirb 
undan **check_order** va **successfully_payment** ni davom etiramiza
check_order funksiyadan bizaga buyurtmaning raqami keladi va narxi
biza buyurtma bor yoki yoligini tekshirishmiza kerak va narxi narxiga tori keldimi
yoki yomi.Pasdigi 3ta variantdan bitasini qaytarishimiza kerak

**#check_order**
```
ORDER_FOUND = # buyurtma topildi xammasi yaxwi 
ORDER_NOT_FOUND = # buyurtma topilmadi 
INVALID_AMOUNT = # buyurtma topildi narxi tori kelmadi
```


!!! successfully_payment
    Bu funkisiyada bizaga puli tolangan buyurtmaning idsi beradi va transaction klassini objecti.


views.py
```python
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz

class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        return self.ORDER_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        print(order_id)

class TestView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment
```
urls.py

```python
from django.urls import path
urlpatterns = [
    path('click/transaction/',TestView.as_view())
]
```

Viewni url ga qoshdik endi click.exe programmasi
bilan test qilb korsak boladi

![alt text](https://i.imgur.com/jC6EN5D.png)

* [ClickUz application](http://docs.click.uz/wp-content/uploads/2018/05/NEW-CLICK_API.zip)
* [ClickUz Documentation](https://docs.click.uz/click-api-testing/)
