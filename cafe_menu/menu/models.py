from django.db import models
from django.template.context_processors import request


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Item(models.Model):
    name=models.CharField(max_length=50)
    ingredients=models.TextField(max_length=500)
    image=models.ImageField(null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.IntegerField(null=True)



class Tables(models.Model):
    table_number=models.PositiveSmallIntegerField()
    is_booked=models.BooleanField(default=False)

class LogOrders(models.Model):
    orders = models.ManyToManyField(Item, related_name='orders')
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")