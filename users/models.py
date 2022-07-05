from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
