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
    slug = models.CharField(default=str(name).lower().replace(' ', '-'), max_length=150, unique=True, verbose_name='slug name', **NULLABLE)
    author = models.CharField(default='admin@gmail.com', max_length=40, verbose_name='опубликовал', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='публикация')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            (
                'set_published',
                'Может активировать/деактивировать публикацию'
            ),
            (
                'change_description',
                'Может изменять описание продукта'
            ),
            (
                'change_category',
                'Может изменять категорию продукта'
            ),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.CharField(max_length=50, verbose_name='номер версии')
    name = models.CharField(max_length=50, verbose_name='название версии', **NULLABLE)
    current = models.BooleanField(default=True, verbose_name='признак актуальной версии')

    def __str__(self):
        return f'Версия продукта "{self.product}": {self.number}'

    class Meta:
        verbose_name = 'версия продукта'
        verbose_name_plural = 'версии продукта'