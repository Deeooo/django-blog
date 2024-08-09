from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    # ready()方法：这个方法会在应用启动时被调用，可以在这里执行一些初始化操作
    def ready(self):
        # 在应用启动时，执行users.signals模块中的代码
        import users.signals
