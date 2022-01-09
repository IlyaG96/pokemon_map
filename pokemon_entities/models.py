from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(default="Описание", null=True)
    title_en = models.CharField(default="На английском", max_length=200)
    title_jp = models.CharField(default="На японском", max_length=200)
    previous_evolution = models.ForeignKey("self",
                                           on_delete=models.SET_NULL,
                                           default=None,
                                           null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=None)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)
    level = models.PositiveIntegerField(default=1)
    health = models.PositiveIntegerField(default=1)
    strength = models.PositiveIntegerField(default=1)
    defence = models.PositiveIntegerField(default=0)
    stamina = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id} {self.pokemon}"



