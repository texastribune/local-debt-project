from django.contrib.gis.db import models


class Collection(models.Model):
    """
    A collection of related shapes.
    """

    name = models.CharField(max_length=255, unique=True)
    authority = models.CharField(max_length=255)
    last_updated = models.DateField()
    count = models.IntegerField()
    slug = models.SlugField(max_length=255)
    source_url = models.URLField(max_length=255)

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return unicode(self.name)


class Shape(models.Model):
    """
    A shape that represents an area.
    """

    collection = models.ForeignKey(Collection, related_name='shapes')
    name = models.CharField(max_length=255)
    identifier = models.IntegerField()
    shape = models.MultiPolygonField(srid=4326)
    slug = models.SlugField(max_length=255)

    objects = models.GeoManager()

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return unicode(self.name)
