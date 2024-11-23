from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class RefreshToken(models.Model):
    user = models.ForeignKey(
        User,  # Связываем с моделью User
        on_delete=models.CASCADE,  # Если пользователь удалён, удаляются все связанные токены
        related_name="refresh_tokens_in_orders"  # Обратная связь
    )
    revoked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Token for {self.user.username}"
