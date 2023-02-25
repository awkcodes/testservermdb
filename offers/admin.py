from django.contrib import admin
from .models import Offer,  Location, Category, Subcategory, Pictures, OfferDate

admin.site.register(OfferDate)
admin.site.register(Offer)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Pictures)
