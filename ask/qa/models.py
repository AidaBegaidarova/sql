from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    object = QuestionManager()
    tittle = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='question_likes_user')

    def get_url(self):
        return '/question/' + str(self.pk) + '/'

    class Meta:
        ordering = ('-id',)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


