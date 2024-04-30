from django.contrib import admin
from .models import Regi
from .models import UserData,Destination


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("fullname", "user", "email", "password", "contact", "city", "address")


admin.site.register(Regi, RegistrationAdmin)


class UserDataAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "desc", "date")


admin.site.register(UserData, UserDataAdmin)


class DestinationAdmin(admin.ModelAdmin):
    list_display = ("image", "place", "description")


admin.site.register(Destination, DestinationAdmin)
