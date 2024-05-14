from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Material(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='materials/', verbose_name='изображение продукта', **NULLABLE)
    create_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    publish = models.BooleanField(default=True, verbose_name='опубликован')
    views_counter = models.PositiveIntegerField(default=0, verbose_name='количество просмотров', help_text='укажите количество просмотров')
    slug = models.CharField(default=str(title).lower().replace(' ', '-'), max_length=150, unique=True, verbose_name='slug name', **NULLABLE)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'