from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, SignUpSerializer, PostPhotoSerializer, PostVideoSerializer, CommentSerializer, UserSerializer
from .models import User, PostPhoto, PostVideo, Comment


# class SignUpAPIView(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request):
#         serializer = SignUpSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignUpAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()


class LoginAPIView(generics.ListCreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

# class LoginAPIView(APIView):
#     permission_classes = (permissions.AllowAny,)
    
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ImageAPIView(generics.ListCreateAPIView):
    serializer_class = PostPhotoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.postphoto_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostVideoAPIView(generics.ListCreateAPIView):
    serializer_class = PostVideoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.postvideo_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.comment_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer














# from django.shortcuts import render
# from rest_framework import  status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import User
# from .serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.parsers import MultiPartParser, FormParser
# from .serializers import PostSerializer
# Create your views here.


# class LoginView(APIView):
#     def post(self, request, format=None):
#         phone_number = request.data.get('phone_number')
#         password = request.data.get('password')

#         try:
#             user = User.objects.get(phone_number=phone_number)
#         except User.DoesNotExist:
#             return Response({'error': 'Invalid phone number or password'}, status=status.HTTP_401_UNAUTHORIZED)

#         if user.password != password:
#             return Response({'error': 'Invalid phone number or password'}, status=status.HTTP_401_UNAUTHORIZED)

#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
    

# class PostView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [IsAuthenticated]

#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)