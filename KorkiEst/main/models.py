from django.db import models


class ProgLang(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Язык программировния'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

class Course(models.Model):
    progLang = models.ForeignKey(ProgLang, related_name='language', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='Языки/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    