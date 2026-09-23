from django.contrib import admin

from .models import Documents, Expense, Income

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Documents)
