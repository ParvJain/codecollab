from django.db import models
from django.contrib.auth.models import User

class Coder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

class Code(models.Model):
    coder_id = models.ForeignKey(Coder, on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    snippet = models.TextField()
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta:
       permissions = (
            ("can_reivew_code", "Can add comments to the code"),
        )

class Comment(models.Model):
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Coder, on_delete=models.CASCADE)
    comment = models.TextField()

class Spy(models.Model):
    user = models.ForeignKey(User)
    action = models.CharField(max_length=100)
