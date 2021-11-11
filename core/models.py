
from django.db import models


class Wefunder(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField(blank=True,null=True)
    pdf_file = models.FileField(upload_to='upload/')

    # def __str__(self):
    #     return self.title

    def delete(self, *args, **kwargs):
        self.pdf_file.delete()
        super().delete(*args, **kwargs)

class WefunderImg(models.Model):
    pdf_id = models.IntegerField(default=0)
    img_file = models.FileField(upload_to='upload/',blank=True)


    def delete(self, *args, **kwargs):

        self.img_file.delete()
        super().delete(*args, **kwargs)

class WefunderSqla(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField(blank=True,null=True)
    pdf_file = models.FileField(upload_to='upload/')
    img_file = models.FileField(blank=True)



