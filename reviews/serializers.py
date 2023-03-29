from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class TinyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "payload",
            "rating",
        )
