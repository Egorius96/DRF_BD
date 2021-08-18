from django.db import models


class EmployeeModel(models.Model):
    device = models.CharField(max_length=50)
    configuration = models.URLField(max_length=100, blank=True)
    price = models.CharField(max_length=50)
    paid_by = models.CharField(max_length=50)
    used_by = models.CharField(max_length=50)
    image = models.ImageField(verbose_name='image', blank=True,
                              upload_to='employee/static/images')
    team = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    item_number = models.PositiveSmallIntegerField()
    empl_start_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.used_by
