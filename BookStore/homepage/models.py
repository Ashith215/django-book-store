from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Booksupload(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to = 'books_Images/')
    count = models.IntegerField(default = 1)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    products = models.ManyToManyField(Booksupload)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)



class cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # since product added in CartItem - class
    # product = models.ManyToManyField(Booksupload)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Cartitem(models.Model):
    user = models.ForeignKey(cart, on_delete = models.CASCADE, null = True, blank = True)
    product = models.ForeignKey(Booksupload, on_delete = models.CASCADE)
    cart_count = models.IntegerField(default = 1)



class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Booksupload, on_delete = models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices = [(i, str(i)) for i in range(1,6)])
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


