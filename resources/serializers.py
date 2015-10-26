from __future__ import unicode_literals

from rest_framework import serializers

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship,
)


# Field that returns dictionary which includes name and URL of model
class NameHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def __init__(self, view_name=None, **kwargs):
        super(NameHyperlinkedRelatedField, self).__init__(view_name, **kwargs)

    def to_representation(self, value):
        url = super(NameHyperlinkedRelatedField, self).to_representation(value)
        return {"name": unicode(value), "url": url}

# Serializer that uses NameHyperlinkedRelatedField
class NameHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    _related_class = NameHyperlinkedRelatedField

class PeopleSerializer(NameHyperlinkedModelSerializer):

    class Meta:
        model = People
        fields = (
            "name",
            "height",
            "mass",
            "hair_color",
            "skin_color",
            "eye_color",
            "birth_year",
            "gender",
            "homeworld",
            "films",
            "species",
            "vehicles",
            "starships",
            "created",
            "edited",
            "url",
        )


class PlanetSerializer(NameHyperlinkedModelSerializer):

    class Meta:
        model = Planet
        fields = (
            "name",
            "rotation_period",
            "orbital_period",
            "diameter",
            "climate",
            "gravity",
            "terrain",
            "surface_water",
            "population",
            "residents",
            "films",
            "created",
            "edited",
            "url"
        )


class FilmSerializer(NameHyperlinkedModelSerializer):

    class Meta:
        model = Film
        fields = (
            "title",
            "episode_id",
            "opening_crawl",
            "director",
            "producer",
            "release_date",
            "characters",
            "planets",
            "starships",
            "vehicles",
            "species",
            "created",
            "edited",
            "url"
        )


class SpeciesSerializer(NameHyperlinkedModelSerializer):

    class Meta:
        model = Species
        fields = (
            "name",
            "classification",
            "designation",
            "average_height",
            "skin_colors",
            "hair_colors",
            "eye_colors",
            "average_lifespan",
            "homeworld",
            "language",
            "people",
            "films",
            "created",
            "edited",
            "url"
        )


class VehicleSerializer(NameHyperlinkedModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            "name",
            "model",
            "manufacturer",
            "cost_in_credits",
            "length",
            "max_atmosphering_speed",
            "crew",
            "passengers",
            "cargo_capacity",
            "consumables",
            "vehicle_class",
            "pilots",
            "films",
            "created",
            "edited",
            "url"
        )


class StarshipSerializer(NameHyperlinkedModelSerializer):

    class Meta:
        model = Starship
        fields = (
            "name",
            "model",
            "manufacturer",
            "cost_in_credits",
            "length",
            "max_atmosphering_speed",
            "crew",
            "passengers",
            "cargo_capacity",
            "consumables",
            "hyperdrive_rating",
            "MGLT",
            "starship_class",
            "pilots",
            "films",
            "created",
            "edited",
            "url"
        )

