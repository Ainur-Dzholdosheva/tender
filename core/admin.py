from django.contrib import admin

from .models import RedFlag, Tender, Buyer, Seller, RedFlag

admin.site.register(Tender)
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(RedFlag)