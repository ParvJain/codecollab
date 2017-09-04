from django.contrib import admin
from .models import Code, Coder, Comment
# Register your models here.
admin.site.register(Code)
admin.site.register(Coder)
admin.site.register(Comment)
