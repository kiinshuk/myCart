from django.db import models

# Create your models here.
class Product(models.Model):
	product_id = models.AutoField
	product_name = models.CharField(max_length=50)
	category = models.CharField(max_length=50, default="")
	subcategory = models.CharField(max_length=50, default="")
	price = models.IntegerField(default=0)
	desc = models.CharField(max_length=300)
	pub_date = models.DateField()
	image = models.ImageField(upload_to="shop/images", default="")

	def __str__(self):
		return self.product_name


class Contact(models.Model):
	msgid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=70, default="")
	subject = models.CharField(max_length=70, default="")
	desc = models.CharField(max_length=500, default="")


class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    cart_json = models.TextField(default="{}")  # default empty JSON
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Order {self.orderid} - {self.name}"