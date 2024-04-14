from django.contrib import admin
from .models import Budget 

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("id", "value", "member", "created_at", "updated_at", )