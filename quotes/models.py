from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=200)
    def __str__(self):
        return self.author_name

class Quote(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    quote_text = models.TextField()
    def __str__(self) :
        return self.quote_text[:200]