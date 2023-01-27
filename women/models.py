from django.db import models


class WomenPost(models.Model):
    title = models.CharField(max_length=222)
    content = models.TextField()
    img = models.ImageField(upload_to='womanPost')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

