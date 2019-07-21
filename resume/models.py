from django.db import models


class LifeEvent(models.Model):
    title = models.CharField(max_length=256)
    organization = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, default=None)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('start_date',)
        abstract = True


class Education(LifeEvent):
    pass


class Experience(LifeEvent):
    pass


class Skill(models.Model):
    title = models.CharField(max_length=256)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class Interest(models.Model):
    title = models.CharField(max_length=256)
    order = models.IntegerField(default=1)
    icon = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
