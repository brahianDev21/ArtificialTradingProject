from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    is_profit = models.BooleanField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    content = models.TextField()
    img_filename = models.ImageField(upload_to='trading_intelligence/files/journal_imgs', null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    pair = models.CharField(max_length=15)
    order_type = models.CharField(max_length=15)
    lots = models.FloatField()
    open_datetime = models.DateTimeField()
    close_datetime = models.DateTimeField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    take_profit = models.FloatField(null=True, blank=True)
    stop_loss = models.FloatField()
    commission = models.FloatField()
    operation_balance = models.FloatField(default=0)

    def __str__(self):
        return self.title