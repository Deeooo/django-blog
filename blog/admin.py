from django.contrib import admin
from .models import Post

# 将Post模型注册到Django管理后台。这样就可以在Django的管理后台中看到和管理Post模型的实例
admin.site.register(Post)
