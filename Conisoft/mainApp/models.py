from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    long_description = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    twitter_url = models.CharField(max_length=200)
    facebook_url = models.CharField(max_length=200)
    linkdin_url = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Timeline(models.Model):
    year = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title