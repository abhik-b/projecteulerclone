from django.contrib import admin
from .models import Profile, Achievement
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'problems_solvd', 'id')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Achievement)
