from django.contrib import admin
from .models import Order
from .models import RefreshToken
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at', 'updated_at',)
    list_filter = ('status',)
    search_fields = ('title', 'description')
@admin.register(RefreshToken)
class RefreshTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "revoked", "created_at")
    search_fields = ("user__username",)