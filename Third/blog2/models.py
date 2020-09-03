from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    title = models.CharField(max_length= 200)
    phone = models.IntegerField(default= 0, max_length=50)
    email = models.EmailField(max_length= 50)
    text = models.TextField()
    created_date = models.DateTimeField(default= timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title