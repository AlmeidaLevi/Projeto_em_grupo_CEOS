from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Tabela em que estarão as tarefas da to_do_list
class Task(models.Model):
    title = models.CharField(max_length=255)
    task_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.title}'
