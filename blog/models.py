# 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
# 运行 python manage.py migrate 来应用数据库迁移
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# 帖子模型
class Post(models.Model):
    # default=timezone.now 默认值为当前时间
    # on_delete=models.CASCADE 删除一个用户时，所有与之关联的帖子也将被删除
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
