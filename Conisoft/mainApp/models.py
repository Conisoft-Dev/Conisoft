from django.db import models

# Create your models here.

class Worshop(models.Model):
    name = models.CharField(max_length=200)
    presenter = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date = models.DateTimeField()
    open_slots = models.IntegerField()
    taken_slots = models.IntegerField(default=0)
    zoom_link = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name


# Unused models v
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