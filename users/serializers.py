from rest_framework import serializers
from .models import User
from reviews.serializers import TinyReviewSerializer


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )


class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )


# 유저가 어떤 도시들을 여행했는지, 몇 개의 방을 가지고 있는지, 나에 대한 리뷰도 표시하는 시리얼라이저 만들기
class PublicUserSerializer(serializers.ModelSerializer):

    reviews = TinyReviewSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = User
        fields = (
            "avatar",
            "name",
            "is_host",
            "gender",
            "language",
            "currency",
            "reviews",
        )
