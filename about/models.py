from django.db import models


class About(models.Model):
    """
    About model, displays about message
    """
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=550)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
