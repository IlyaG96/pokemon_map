from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=100,
                                verbose_name="Имя по-русски")
    image = models.ImageField(blank=True,
                              null=True,
                              verbose_name="Картинка")
    description = models.TextField(default="Описание",
                                   null=True,
                                   blank=True,
                                   verbose_name="Описание")
    title_en = models.CharField(default=None,
                                max_length=100,
                                blank=True,
                                verbose_name="Имя по-английски")
    title_jp = models.CharField(default=None,
                                max_length=100,
                                blank=True,
                                verbose_name="Имя по-японски")
    previous_evolution = models.ForeignKey("self",
                                           on_delete=models.SET_NULL,
                                           default=None,
                                           null=True,
                                           blank=True,
                                           related_name="next_evolution",
                                           verbose_name="Предыдущая эволюция")

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = "Покемон"
        verbose_name_plural = "Покемоны"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                default=None,
                                verbose_name="Покемон"
                                )
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=None,
                                       verbose_name="Появился")
    disappeared_at = models.DateTimeField(default=None,
                                          verbose_name="Исчезнет")
    level = models.PositiveIntegerField(default=1,
                                        verbose_name="Уровень")
    health = models.PositiveIntegerField(default=1,
                                         verbose_name="Здоровье")
    strength = models.PositiveIntegerField(default=1,
                                           verbose_name="Сила")
    defence = models.PositiveIntegerField(default=1,
                                          verbose_name="Защита")
    stamina = models.PositiveIntegerField(default=1,
                                          verbose_name="Выносливость")

    def __str__(self):
        return f"{self.id} {self.pokemon}"

    class Meta:
        verbose_name = "Вид покемона"
        verbose_name_plural = "Видов покемонов"



