from django.db import models

# Create your models here.

class Item(models.Model):
    title= models.CharField(max_length=100)
    price= models.IntegerField()
    discount_price= models.IntegerField()
    category = models.CharField(max_length=100)
    label = models.CharField(max_length=50)
    stock_no = models.IntegerField()
    description_short = models.TextField()
    description_long = models.TextField()
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title
    


