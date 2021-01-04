from django.db import models

from django.contrib.auth import get_user_model

from django.db.models.options import Options

User = get_user_model()


class Post(models.Model):
    Options.verbose_name = "post"
    Options.verbose_name_plural = "posts"
    text = models.TextField("post's text")
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts",
                               verbose_name="post's author")
    group = models.ForeignKey("Group", on_delete=models.SET_NULL,
                              related_name="posts",
                              blank=True,
                              verbose_name="post's group", null=True)

    class Meta:
        ordering = ['-pub_date']


class Group(models.Model):
    Options.verbose_name = "group"
    Options.verbose_name_plural = "groups"
    title = models.CharField("group's title", max_length=200)
    slug = models.SlugField("group's url", unique=True)
    description = models.TextField("group's details")

    def __str__(self):
        return self.title
