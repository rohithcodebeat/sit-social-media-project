from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
# UserModel -> Authentication 


class UsersProfileModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="user_profile_models_user")
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="user-profile/",null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    facebook = models.URLField(null=True, blank=True) 
    linkedin = models.URLField(null=True, blank=True)
    whatapp = models.URLField(null=True, blank=True) # https://wa.me/91987654210
    email = models.EmailField(max_length=100, null=True, blank=True) # name@domain.in

    created_at = models.DateTimeField(auto_now_add=True)







