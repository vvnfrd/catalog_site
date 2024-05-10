from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='название категории')
    description = models.TextField(max_length=250, verbose_name='описание категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='название продукта')
    description = models.TextField(max_length=250, verbose_name='описание продукта')
    image = models.ImageField(upload_to='products/', verbose_name='изображение продукта', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена продукта')
    create_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    update_at = models.DateField(auto_now=True, verbose_name='дата изменения')
    views_counter = models.PositiveIntegerField(default=0, verbose_name='количество просмотров', help_text='укажите количество просмотров')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'