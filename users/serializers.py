from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'password')

    def create(self, validated_data):
        """Create a new user"""
        return get_user_model().objects.create_user(**validated_data)
