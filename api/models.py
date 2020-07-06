from django.db import models

# Create your models here.


# Model for storing activity periods of the members
class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


# Model to display the members
class MembersList(models.Model):
    ok = models.BooleanField(default=False)


# Model representing the member
class User(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)
    activity_periods = models.ManyToManyField(ActivityPeriod, related_name='Users')
    list = models.ForeignKey(MembersList, on_delete=models.CASCADE, null=True, related_name='members')

    def __str__(self):
        return self.real_name














