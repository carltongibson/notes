from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=30)


class OtherArticle(models.Model):
    class Meta:
        db_table = "article"

    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
