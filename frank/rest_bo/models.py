from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    display_order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('name',)

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, null=True)
    level = models.PositiveSmallIntegerField(null=True)
    category = models.ForeignKey('Category', related_name='skills')

    class Meta:
        ordering = ('name',)

class Education(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_description = models.CharField(max_length=255, null=True)
    year_in = models.DateField()
    year_out = models.DateField(null=True)
    place = models.CharField(max_length=50)
    diploma = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    extra_info = models.TextField(null=True)
    description = models.TextField(null=True)
    skills = models.ManyToManyField(Skill)

    class Meta:
        ordering = ('year_in',)

class Experience(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    date_in = models.DateField()
    date_out = models.DateField(null=True)
    place = models.CharField(max_length=50)
    website = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    accomplishments = models.TextField()
    display_order = models.PositiveSmallIntegerField()
    skills = models.ManyToManyField(Skill)

    class Meta:
        ordering = ('date_in',)

class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=50, null=True)
    level = models.PositiveSmallIntegerField(null=True)
    category = models.ForeignKey('Category', related_name='interests')
    display_order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('name',)

class Travel(models.Model):
    place = models.CharField(max_length=50, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    display_order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('place',)