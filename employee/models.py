from django.db import models


class Employee(models.Model):
    image = models.ImageField(verbose_name='image', blank=True,
                              upload_to='employee/static/images')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    team = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Employees'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Device(models.Model):
    device = models.CharField(max_length=100)
    configuration = models.URLField(max_length=250, blank=True)
    price = models.PositiveSmallIntegerField()
    paid_by = models.CharField(max_length=50)
    used_by = models.ForeignKey(Employee, verbose_name='Used by', on_delete=models.SET_NULL, null=True, blank=True)
    item_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.device

    class Meta:
        db_table = 'Devices'
        verbose_name_plural = 'Devices'