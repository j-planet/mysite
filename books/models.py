from django.db import models


# -------- helper classes ------------

class BookManager(models.Manager):
    def title_count(self, title):
        return self.filter(title__icontains=title).count()


class AwesomeBookManager(models.Manager):
    def get_query_set(self):
        return super(AwesomeBookManager, self).get_query_set().filter(authors__first_name__icontains='awesome')


# -------- Model classes ------------

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return u'%d - %s' % (self.id, self.name)

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    last_accessed = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()
    awesome_objects = AwesomeBookManager()

    def __unicode__(self):
        return self.title


