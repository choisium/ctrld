from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
# 필요한 모델: User, Profile(if needed), Genre, Calendar, Event, Schedule

class User(AbstractUser):
    pass

class Genre(models.Model):
    name = models.CharField(max_length=20)

def cal_batch():
    now = int("{:%Y}".format(datetime.now()))
    return now - 1994

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', related_query_name='user')
    genre = models.ManyToManyField(Genre, related_name='genrers', related_query_name='genrer')
    batch = models.IntegerField(default = cal_batch())

class Calendar(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.id + ": " + self.name

class Event(models.Model):
    calendarId = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name="schedules", related_query_name="schedule")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_schedules', related_query_name='my_schedule')
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=5000)        # 추후 이미지도 들어갈 수 있나 확인해봐야 함
    media = models.FileField(upload_to='schedules/')
    genre = models.ManyToManyField(Genre, related_name='genre_schedules', related_query_name='genre_schedule')
    
    def __str__(self):
        return str(self.calendarId) + ": " + self.title

class RecurrenceRule(models.Model):
    FREQUENCY_CHOICES = [('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')]
    BY_DAY_CHOICIES = [('SUN', 'SUN'), ('MON', 'MON'), ('TUE', 'TUE'), ('WED', 'WED'), ('THU', 'THU'), ('FRI', 'FRI'), ('SAT', 'SAT')]
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    frequency = models.CharField(choices = FREQUENCY_CHOICES, default='Weekly', max_length=30)
    interval = models.IntegerField(default = 1)
    byweeknumber = models.BooleanField(default = False)
    byday = models.CharField(choices = BY_DAY_CHOICIES, max_length=3)

class RemovedRecurredSchedule(models.Model):
    rule = models.ForeignKey(RecurrenceRule, on_delete=models.CASCADE)
    old_start = models.DateField()
    old_end = models.DateField()
    new_start = models.DateField(blank=True, null=True)
    new_end = models.DateField(blank=True, null=True)

class Schedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='events', related_query_name='event')
    parentSchedule = models.ForeignKey("self", on_delete=models.CASCADE, related_name='children', related_query_name='child', null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(max_length=30, default='미정')
    recurrenceRule = models.OneToOneField(RecurrenceRule, on_delete=models.SET_NULL, null=True, blank=True)
    isAllDay = models.BooleanField(default=False)
    isPrivate = models.BooleanField(default=False)      # 나만 볼 일정인지
    isOpen = models.BooleanField(default=True)          # 컨디 외부에 공개될 행사인지, 컨디 회원만 확인할 수 있는 행사인지

    def __str__(self):
        return str(self.event) + ": " + str(self.start)

# FREQUENCY_CHOICES = [('Daily', 'Daily'), ('Monthly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')]
# BY_DAY_CHOICIES = [('SUN', '일요일'), ('MON', '월요일'), ('TUE', '화요일'), ('WED', '수요일'), ('THU', '목요일'), ('FRI', '금요일'), ('SAT', '토요일')]
# COUNT : 총 몇 회 반복
# INTERVAL : 몇 주마다 반복
 