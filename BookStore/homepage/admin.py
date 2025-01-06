from django.contrib import admin
from .models import Book, Booksupload, wishlist, cart, Cartitem, BookReview

admin.site.register(Book)
admin.site.register(wishlist)
admin.site.register(cart)
admin.site.register(Cartitem)


class BooksuploadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'image', 'count')
    list_filter = ('name', 'description', 'price')
    search_fields = ['name', 'description', 'price']


admin.site.register(Booksupload, BooksuploadsAdmin)

# class CartitemAdmin(admin.ModelAdmin):
#     list_display = ('id')

# admin.site.register(Cartitem, CartitemAdmin)


# class BookReviewAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'review_text', 'rating')
#     list_filter = ('rating', 'product')
admin.site.register(BookReview)


