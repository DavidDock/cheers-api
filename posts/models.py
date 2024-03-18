from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200, blank=True) 
    content = models.TextField(max_length=550, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_lawdck', blank=True
    )
    rating = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    score = models.IntegerField(choices=rating, default=5, validators=[
                                MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
