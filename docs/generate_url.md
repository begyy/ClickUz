#Url yaratish

Click.uz saytiga yuborish uchun biza url yaratishmiza kerak
bu url klientga korsatiladi va urlga kirganida klient pul tolash qismiga otib ketadi

![alt text](https://i.imgur.com/AnX0wSd.png)
```python
from clickuz import ClickUz

url = ClickUz.generate_url(order_id='172',amount='150000')
print(url)
```

!!! return_url
    Agar klient pul tolab bolganidan keyn saytga qaytib kelishini xoxlasangiz
    *return_url* ga ozingizni domain qoshib qoyishiz kerak boladi

```python
from clickuz import ClickUz

url = ClickUz.generate_url(order_id='172',amount='150000',return_url='http://example.com')
print(url)
```
Klient pul tolab bolganidan keyn sizning saytizga qaytib keladi