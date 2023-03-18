from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User,PostPhoto,PostVideo , Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'full_name', 'date_of_birth', 'email', 'postal_code', 'occupation', 'experience', 'password',]


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('phone_number', 'password')
    
    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        if phone_number and password:
            user = authenticate(request=self.context.get('request'),
                                phone_number=phone_number, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "phone_number" and "password".'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
    
    
    
        

class SignUpSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('full_name', 'date_of_birth', 'email', 'postal_code', 'occupation', 'experience', 'password', 're_password')

    def validate(self, attrs):
        password = attrs.get('password')
        re_password = attrs.get('re_password')

        if password != re_password:
            raise serializers.ValidationError('Password does not match')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

    

class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        fields = ('id', 'user', 'image', 'description', 'created_at')
        read_only_fields = ('id', 'created_at')

class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ('id', 'user', 'video', 'description', 'created_at')
        read_only_fields = ('id', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'comment', 'created_at')
        read_only_fields = ('id', 'created_at')



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



# def validate(self, attrs):
#         phone_number = attrs.get('phone_number')
#         email = attrs.get('email')
#         password = attrs.get('password')
#         re_password = attrs.get('re_password')

#         if password != re_password:
#             raise serializers.ValidationError('Password and Re-Password must match')
#         user_qs = User.objects.filter(phone_number=phone_number)
#         if user_qs.exists():
#             raise serializers.ValidationError('Phone number is already taken')
#         user_qs = User.objects.filter(email=email)
#         if user_qs.exists():
#             raise serializers.ValidationError('Email is already taken')
#         return attrs

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)