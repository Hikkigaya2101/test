from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Position(models.Model):
    position_name = models.TextField(null=True)

    def __str__(self):
        return f'{self.position_name}'

class Worker(models.Model):
    fio_worker = models.TextField()
    born_date = models.DateField(null=True)
    work_date = models.DateField(null=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT, null=True)
    img = models.ImageField(upload_to='img/',null='True')

    class Meta:
        ordering = ['-id']
        verbose_name = 'ФИО'
        verbose_name_plural = 'ФИО'

    def __str__(self):
        return f' {self.fio_worker}'

