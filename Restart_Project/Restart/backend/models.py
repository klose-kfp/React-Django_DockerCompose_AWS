from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class GPTModel(models.Model):
    loginuser = models.CharField(max_length=50, blank=True)

    author = models.CharField(
        max_length=50,
    )
    Title = models.TextField()
    text = models.TextField()
    Mermaid = models.TextField()
    svg = models.TextField()
    UpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "GPT"

    def __str__(self):
        return str(self.Title)
