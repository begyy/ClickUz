#Url yaratish

![alt text](https://i.imgur.com/jHZCGqL.jpg)

Click.uz saytiga yuborish uchun biza url yaratishmiza kerak
bu url klientga korsatiladi va urlga kirganida klient pul tolash qismiga otib ketadi

```python
from clickuz import ClickUz

url = ClickUz.generate_url(order_id='77',amount='500000')
print(url)
```

!!! return_url
    Agar klient pul tolab bolganidan keyn saytga qaytib kelishini xoxlasangiz
    *return_url* ga ozingizni domain qoshib qoyishiz kerak boladi

```python
from clickuz import ClickUz

url = ClickUz.generate_url(order_id='77',amount='500000',return_url='http://example.com')
print(url)
```
Klient pul tolab bolganidan keyn sizning saytizga qaytib keladi