from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user
