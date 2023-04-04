from rest_framework import serializers
from .models import Perk, Experience
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceListSerializer(serializers.ModelSerializer):

    is_host = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "pk",
            "country",
            "city",
            "name",
            "price",
            "is_host",
        )

    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user


class ExperienceDetailSerializer(serializers.ModelSerializer):

    host = TinyUserSerializer(
        read_only=True,
    )
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )
    category = CategorySerializer(
        read_only=True,
    )

    is_host = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = "__all__"

    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user
