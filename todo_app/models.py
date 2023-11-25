from django.db import models

class todo(models.Model):
    task_name=models.CharField(max_length=300)
    priority=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.task_name


