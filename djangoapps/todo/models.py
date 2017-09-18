from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_text = models.CharField(max_length=200)

    def __str__(self):
        return self.todo_text


class Expire(models.Model):
    todo = models.OneToOneField(Todo)
    expire = models.DateTimeField()

    def __str__(self):
        return self.expire.isoformat()


class Done(models.Model):
    todo = models.OneToOneField(Todo)
    done = models.DateTimeField()

    def __str__(self):
        return self.done.isoformat()
