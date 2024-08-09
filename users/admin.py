from django.contrib import admin
from .models import Profile


# 将Profile模型注册到Django管理后台。这样就可以在Django的管理后台中看到和管理Profile模型的实例
admin.site.register(Profile)
