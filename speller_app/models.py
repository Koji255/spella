from django.db import models
from users.models import User

# Create your models here.
class Text(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # Combination of 4 logenst eng words + 3 symbols as "."
    header = models.CharField(183)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.pk}, {self.header}; user: {self.user_id}"