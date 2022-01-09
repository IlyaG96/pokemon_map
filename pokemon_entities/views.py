import folium
from .models import Pokemon, PokemonEntity
from django.http import HttpResponseNotFound
from django.shortcuts import render


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision"
    "/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832"
    "&fill=transparent"
)


def make_abs_uri(request, pokemon):
    if pokemon.image:
        return request.build_absolute_uri(pokemon.image.url)
    return DEFAULT_IMAGE_URL


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemons = Pokemon.objects.all().only("image", "id", "title_ru")
    for pokemon in pokemons:
        pokemon_entity = \
            PokemonEntity.objects.filter(pokemon=pokemon).only("lat", "lon")
        for entity in pokemon_entity:
            add_pokemon(
                    folium_map,
                    entity.lat,
                    entity.lon,
                    make_abs_uri(request, pokemon)
                )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            "pokemon_id": pokemon.id,
            "img_url": make_abs_uri(request, pokemon),
            "title_ru": pokemon.title_ru,
        })

    return render(request, "mainpage.html", context={
        "map": folium_map._repr_html_(),
        "pokemons": pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon = pokemon
            break
    else:
        return HttpResponseNotFound("<h1>Такой покемон не найден</h1>")

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemon_entities = \
        PokemonEntity.objects.filter(pokemon=requested_pokemon).only("lat", "lon")
    for entity in pokemon_entities:
        add_pokemon(
            folium_map,
            entity.lat,
            entity.lon,
            make_abs_uri(request, pokemon)
        )

    pokemon = {
        "pokemon_id": requested_pokemon.id,
        "title_ru": requested_pokemon.title_ru,
        "title_en": requested_pokemon.title_en,
        "title_jp": requested_pokemon.title_jp,
        "description": requested_pokemon.description,
        "img_url": make_abs_uri(request, requested_pokemon)
    }

    previous_evolution = requested_pokemon.previous_evolution

    if previous_evolution:
        pokemon["previous_evolution"] = {
            "title_ru": previous_evolution.title_ru,
            "pokemon_id": previous_evolution.id,
            "img_url": make_abs_uri(request, previous_evolution)
        }

    next_evolution = requested_pokemon.next_evolution.all()

    if next_evolution:
        next_evolution = next_evolution[0]
        pokemon["next_evolution"] = {
            "title_ru": next_evolution.title_ru,
            "pokemon_id": next_evolution.id,
            "img_url": make_abs_uri(request, next_evolution)
        }

    return render(request, "pokemon.html", context={
        "map": folium_map._repr_html_(), "pokemon": pokemon,
    })
