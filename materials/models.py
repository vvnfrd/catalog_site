from django.db import models

class Material(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='materials/', verbose_name='изображение продукта', blank=True, null=True)
    create_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    publish = models.BooleanField(default=True, verbose_name='опубликован')
    views_counter = models.PositiveIntegerField(default=0, verbose_name='количество просмотров', help_text='укажите количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'