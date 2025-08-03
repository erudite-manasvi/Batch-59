from rest_framework import serializers
from . models import user
# class UserSerializer(serializers.Serializer):
#     fullname=serializers.CharField(max_length=100)
#     country=serializers.CharField(max_length=50)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= user
        fields= ['id',"fullname","country"]