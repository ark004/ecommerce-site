from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager,self).get_queryset().filter(active=True)

class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)

    class meta:
        ververse_name_plural= 'categories'
        
    def get_absolute_url(self):
        return reverse('e_app:category_list',args=[self.slug])    


    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product', on_delete=models.CASCADE)   
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='product_creator')  
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255,default='admin')
    desc=models.TextField(max_length=255,blank='True')
    image=models.ImageField(upload_to='images/',default='images/default.jpg')
    slug=models.SlugField(max_length=120)
    price=models.DecimalField(decimal_places=2,max_digits=4)
    in_stock=models.BooleanField(default=True)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    objects= models.Manager()
    product=ProductManager()

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('e_app:product_detail',args=[self.slug])    

    def __self__(self):
        return self.title    
   