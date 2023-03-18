from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, date_of_birth, email, postal_code, occupation, experience, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number must be set')
        if not full_name:
            raise ValueError('The full name must be set')
        if not email:
            raise ValueError('The email must be set')
        if not date_of_birth:
            raise ValueError('The date of birth must be set')
        if not postal_code:
            raise ValueError('The postal code must be set')
        if not occupation:
            raise ValueError('The occupation must be set')
        if not experience:
            raise ValueError('The experience must be set')
        user = self.model(phone_number=phone_number, full_name=full_name, date_of_birth=date_of_birth, email=self.normalize_email(email), postal_code=postal_code, occupation=occupation, experience=experience, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, date_of_birth, email, postal_code, occupation, experience, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, full_name, date_of_birth, email, postal_code, occupation, experience, password, **extra_fields)

class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=20, unique=True,default='0000000000')
    full_name = models.CharField(max_length=100, default='Full Name')
    date_of_birth = models.DateField(default='2000-01-01')
    email = models.EmailField(max_length=100)
    postal_code = models.CharField(max_length=10, default='00000')
    occupation = models.CharField(max_length=100, default='Occupation')
    experience = models.CharField(max_length=100, default='Experience')
    

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name', 'date_of_birth', 'email', 'postal_code', 'occupation', 'experience']

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def name(self):
        return self.full_name

class PostPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
    
class PostVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostPhoto, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'

# from django.db import models
# Create your models here.


# class User(models.Model):
#     phone_number = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=128)

#     def __str__(self):
#         return self.phone_number
    

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/', null=True, blank=True)
#     video = models.FileField(upload_to='videos/', null=True, blank=True)
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user.username} - {self.created_at}'




# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     price = models.FloatField()
#     image = models.ImageField(upload_to='product_images')
#     category = models.ForeignKey('Category', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name