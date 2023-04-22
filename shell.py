from app.models import *

Category.objects.create(name="продукты")
Category.objects.create(name="мыломойка")

Product.objects.create(name='хлеб',price=20,category_id=1)
Product.objects.create(name='вода',price=45,category_id=1)
Product.objects.create(name='моющее средство для посуды',price=150,category_id=2)
Product.objects.create(name='порошок',price=320,category_id=2)
Product.objects.create(name='шампунь',price=500,category_id=2)