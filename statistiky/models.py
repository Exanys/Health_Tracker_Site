from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, verbose_name='Age')
    password = models.CharField(max_length=30, unique=True, verbose_name='Password')
    country = models.CharField(max_length=3, null=True, verbose_name='Country')
    email = models.EmailField(unique=True, null=False, verbose_name='Email')
    serial_number = models.CharField(max_length=30, unique=True, null=False, verbose_name='Serial number')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Person'


class Temperature(models.Model):
    min_value = models.FloatField(null=False, verbose_name='Min value')
    max_value = models.FloatField(null=False, verbose_name='Max value')
    avarage_value = models.FloatField(null=False, verbose_name='Avarage value')

    def __str__(self):
        return 'Temperature'

    class Meta:
        verbose_name = 'Temperature'


class Heart_rate(models.Model):
    min_value = models.IntegerField(null=False, verbose_name='Min value')
    max_value = models.IntegerField(null=False, verbose_name='Max value')
    avarage_value = models.FloatField(null=False, verbose_name='Avarage value')

    def __str__(self):
        return 'Heart rate'

    class Meta:
        verbose_name = 'Heart rate'

class Sleep(models.Model):
    """There will by fields for length of sleep, wake up time, number of wake ups,
    and number of sleep overs"""
    length = models.TimeField(null=False, verbose_name='Length of sleep')
    wake_up_time = models.TimeField(null=False, verbose_name='Wake up time')
    number_of_wake_ups = models.IntegerField(null=False, verbose_name='Number of wake ups')
    deep_sleep = models.FloatField(null=False, verbose_name='Deep sleep')

    def __str__(self):
        return 'Sleep'

    class Meta:
        verbose_name = 'Sleep'


class Statistic(models.Model):
    #connected to person and other field with names temperature, heart_rate and sleep will be connected to new records
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)
    heart_rate = models.ForeignKey(Heart_rate, on_delete=models.CASCADE)
    sleep = models.ForeignKey(Sleep, on_delete=models.CASCADE)
    date = models.DateField(null=False, verbose_name='Date')

    def __str__(self):
        return 'Statistic'

    class Meta:
        verbose_name = 'Statistic'
        ordering = ['date']
