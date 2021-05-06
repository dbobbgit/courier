from django.db import models
from django.utils import timezone

# Create your models here.
"""
Author:
- name
- byline (optional)


Article:
- body
- author
- post_created
- title
"""

class Author(models.Model):
    name = models.CharField(max_length=50)
    byline = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        """Returns the name of the author any time the Author instance is asked for"""
        return self.name

class Article(models.Model):
    ...

    body = models.TextField()
    title = models.CharField(max_length=30)
    post_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

