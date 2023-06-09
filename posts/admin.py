from django.contrib import admin
from .models import UserPostsModel, UserSavedPostModel
# Register your models here.

admin.site.register(UserPostsModel)
admin.site.register(UserSavedPostModel)
