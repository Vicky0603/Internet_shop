from django.db import models


# Модель категории товара
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True) # Название категории
    slug = models.SlugField(max_length = 200, unique = True) # Уникальный идентификатор

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

# Модель товара
class Product(models.Model):
    # Категория - вторичный ключ. related_name имя наследуемого объекта БД. on_delete - указываем что у нас каскадное удаление
    category = models.ForeignKey(Category,related_name = 'products', on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, db_index = True) # Название товара
    slug = models.SlugField(max_length = 200, db_index = True) # Идентификатор
    image = models.ImageField(upload_to = 'products/%Y/%m/%d', blank = True) # Изображение товара
    description = models.TextField(blank = True) # Описание товара
    price = models.DecimalField(max_digits = 10, decimal_places = 2) # Цена товара. Параметр Decimal-денежный. 10-чило десятичных цифр. 2- количество знаков после запятой
    available = models.BooleanField(default = True) # Товар в наличии или нет
    created = models.DateTimeField(auto_now_add = True) # Опубликовано
    updated = models.DateTimeField(auto_now = True) # Обновлено

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),) #Определили индекс по двум полям, удобно будет для поиска товара

    def __str__(self):
        return self.name









# Create your models here.
