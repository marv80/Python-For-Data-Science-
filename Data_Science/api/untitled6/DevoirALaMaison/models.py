from django.db import models

# Create your models here.
class Subject(models.Model):
    IDSubject = models.IntegerField()
    AGE = models.IntegerField()
    SPORT = models.IntegerField()
    label = models.FloatField()
    xchest = models.FloatField()
    ychest = models.FloatField()
    zchest = models.FloatField()
    ecg = models.FloatField()
    resp = models.FloatField()
    xwrist = models.FloatField()
    ywrist = models.FloatField()
    zwrist = models.FloatField()
    bvp = models.FloatField()
    temp = models.FloatField()

    #the dependent variable : y
    activity = models.FloatField(null=True)
    #Just to give a date to the creation of the object instance
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Un suject avec un age de {self.AGE}'
