#Ishni boshlash
O'rtanib olganimizdan song **settins.py** ga o'rnatilgan to'plami qo'shib qoyish kerak va **click.uz** dan
olgan **merchant_id** , **service_id**, **secret_key** ni yozib qoyishimiza kerak
```python
INSTALLED_APPS = [
     ...,
    'clickuz',
    'rest_framework'
]

CLICK_SETTINGS = {
    'service_id':'1',
    'merchant_id':'1',
    'secret_key':'1',
    'merchant_user':'1'
}
```
undan song quydagi komandani bajarishimiza kerak yani bazani migrate qilb olish kerak
```
python manage.py migrate
```
