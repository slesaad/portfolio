from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=1)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    video = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
