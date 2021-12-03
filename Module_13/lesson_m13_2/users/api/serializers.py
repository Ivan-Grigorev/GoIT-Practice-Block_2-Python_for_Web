from rest_framework import serializers
from users.models import SportUser


class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SportUser
        fields = ["username"]
