from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # 图像处理工具的库


# 个人资料模型
class Profile(models.Model):
    # 这是一个一对一关系字段，将Profile模型与User模型关联起来。这意味着每个用户只能有一个与之关联的个人资料
    # 当关联的用户被删除时，该个人资料也会被删除（on_delete = models.CASCADE）
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 这是一个图像字段，用于存储用户的个人头像。
    # 默认情况下，如果用户没有上传头像，将使用名为default.jpg的默认图片。上传的图片将被保存到profile_pics目录下。
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} 个人资料'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # 调用父类的save方法来保存对象的基本属性

        # 打开图像
        img = Image.open(self.image.path)

        # 验证图像的大小，并修改尺寸为300，并且保存
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # Image.thumbnail()方法是PIL库中用于创建图像缩略图的功能
            # 主要作用是将原图像按照一定比例缩小
            # thumbnail()不会改变原图像的宽高比。即使给定的尺寸参数是正方形，如果原图像是长方形，则缩略图也会保持相应的长方形比例。
            img.thumbnail(output_size)
            # 调用thumbnail()后，需要使用图像对象的save方法保存更改后的图像到文件。否则，更改只会保留在内存中，不会永久存储。
            img.save(self.image.path)
