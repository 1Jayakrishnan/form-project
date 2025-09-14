from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be a positive number.")
        return value

    def validate_profile(self, value):
        words = value.strip().split()
        if len(words) < 12:
            raise serializers.ValidationError("Profile description must contain at least 12 words.")
        return value