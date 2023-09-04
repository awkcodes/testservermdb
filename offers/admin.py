from django.contrib import admin
from .models import (
    Company,
    Offer,
    Location,
    Category,
    Subcategory,
    Pictures,
    OfferDate,
    Feedbacks,
)

admin.site.register(OfferDate)
admin.site.register(Offer)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Pictures)
admin.site.register(Company)
admin.site.register(Feedbacks)
