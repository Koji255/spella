from django.db import models
from users.models import User

# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Combination of 4 logenst eng words + 3 symbols as "."
    header = models.CharField(48)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return f"Text(id[{self.pk}], header[{self.header}]); user(id[{self.user_id}])"