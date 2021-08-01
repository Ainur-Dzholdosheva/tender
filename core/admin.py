from django.contrib import admin

from .models import Tender, Buyer, Seller

admin.site.register(Tender)
admin.site.register(Buyer)
admin.site.register(Seller)