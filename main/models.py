from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


STATUS = [("dr", "Draft"), ("pu", "Pulblish")]


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    decription = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    img = models.ImageField(upload_to="images", null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default="dr", null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    slug = models.SlugField(max_length=250, null=True, unique_for_date="date")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]

    def get_absolute_url(self):
        return reverse(
            "post-detail",
            args=[self.date.year, self.date.month, self.date.day, self.slug],
        )
