from django.db import models

class Poll(models.Model):
    question=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.question+' is published on '+str(self.pub_date)


class Choice(models.Model):
    poll=models.ForeignKey(Poll)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
