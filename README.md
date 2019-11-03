# DJ-Shopify

A showcase of how Shopify can be intergrated into Django.


### Installing

Firstly clone this repository to your development machine:

```
git clone https://github.com/nishanthc/dj-shopify.git
```

Install the required python packages:

```
pip install -r requirements.txt
```

Add your OWN Shopify API credentials to settings.py:


```
SHOPIFY_API_KEY = '51eb337b30e5de7cb85755b3f090a0a2'

SHOPIFY_PASSWORD = '2dffede1768858155086c5bfecd90d70'

SHOPIFY_STORE_NAME = 'nishio'

SHOPIFY_SHARED_SECRET = 'ebfe5s5cd04b1002f6307b94b4267830'
```

Run migrations:

```
python manage.py migrate

```
Populate Django with your existing products:
```

python manage.py populate_products

```

Create an admin account:

```
python manage.py createsuperuser

```