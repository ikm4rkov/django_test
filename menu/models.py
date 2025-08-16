from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название меню")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="URL")
    named_url = models.CharField(max_length=100, blank=True, null=True, verbose_name="Named URL")
    parent = models.ForeignKey('self', blank=True, null=True, related_name="children", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except:
                return '#'
        return self.url or '#'
