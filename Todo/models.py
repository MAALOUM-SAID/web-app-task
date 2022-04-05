from django.db import models

# Create your models here.

class Task(models.Model):
    categories=(
        ('reading','reading'),
        ('stading','stading'),
        ('sport','sport'),
        ('gaming','gaming'),
    )
    status=(
        ('in progress','in progress'),
        ('pending','pending'),
        ('starting','starting'),
        ('Done','Done'),
    )
    task_title=models.CharField(max_length=50,default="",blank=True,null=True)
    task=models.CharField(max_length=255,blank=True,null=True)
    begin=models.TimeField(blank=True,null=True)
    end=models.TimeField(blank=True,null=True)
    category=models.CharField(max_length=255,choices=categories,default=categories[0],blank=True,null=True)
    status=models.CharField(max_length=50,choices=status,default=status[0],blank=True,null=True)
    def __str__(self):
        if self.task_title==None:
            return 'Null'
        return f"{self.task_title}"
    def __iter__(self):

        return iter([self.id,self.task_title,self.task,self.begin,self.end])
    


