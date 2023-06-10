from django.db import models
from django.contrib.auth import get_user_model

# CRUD -> Create, Read, Update, Delete
# Create your models here.
class UserPostsModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_posts_model_user")
    title = models.CharField(max_length=300, null=True, blank=True)
    media = models.ImageField(upload_to="user-posts/",null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(get_user_model(), related_name="users_post_model_likes", blank=True)

    updated_at = models.DateTimeField(auto_now=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    # saving image = img -> store img in media dir following my specific folder name
    # rendering image = return image address or dir
    # path -> curr/ media/ specifi folder name -> media/user-posts/img_file_name
    # localhost:8000/user/login/
    # path("", include("app.urls")),
    # localhost:8000/ media + image reference (folders + file_name)
    # "media" + "img ref"
    # domain + MEDIA_URL + MEDIA_ROOT
    #         curr-path (BASE_DIR) + media + file_ref (desktop/django-class/project/social-media/projects/media/{file-name})
    # localhost:8000/media/user-posts/screen-shot-2022-09-09:99393.png


class UserSavedPostModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="user_saved_posts_model_user")
    posts = models.ManyToManyField(UserPostsModel, related_name="user_saved_posts", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
