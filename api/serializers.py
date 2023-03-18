from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            user = authenticate(phone_number=phone_number, password=password)
            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials')
        else:
            raise serializers.ValidationError
        

class SignUpSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['phone_number', 'full_name', 'date_of_birth', 'email', 'postal_code', 'occupation', 'experience', 'password', 're_password']

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        email = attrs.get('email')
        password = attrs.get('password')
        re_password = attrs.get('re_password')

        if password != re_password:
            raise serializers.ValidationError('Password and Re-Password must match')
        user_qs = User.objects.filter(phone_number=phone_number)
        if user_qs.exists():
            raise serializers.ValidationError('Phone number is already taken')
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError('Email is already taken')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)




# from rest_framework import serializers
# from .models import User, Post

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['phone_number', 'password']

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'user', 'image', 'video', 'comment', 'created_at')
#         read_only_fields = ('id', 'created_at')