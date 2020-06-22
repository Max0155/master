from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name='Имя позиции')
    description = models.TextField(verbose_name='Описание продукта')
    quantity = models.IntegerField(default=False,verbose_name='В наличии шт.')
    photo = models.ImageField(upload_to=f'photo/%Y/%m/%d/', blank=True, verbose_name='Фотография')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Информация о публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")
    view = models.IntegerField(default=0)


    def get_absolute_url(self): # Абсолютная ссылка на категорию джанго по умолчанию использует это имя в админке
        return reverse('one_product', kwargs={"pk": self.pk}) #название маршрута из urls

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Имя позиции'
        verbose_name_plural = 'Имена позиций'


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Название категории")

    def get_absolute_url(self): # Абсолютная ссылка на категорию джанго по умолчанию использует это имя
        return reverse('category', kwargs={"category_id": self.pk}) #название маршрута из urls

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
