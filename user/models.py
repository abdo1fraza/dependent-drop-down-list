from django.db import models

class College(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.name)

class Branch(models.Model):
    college = models.ForeignKey(College, on_delete = models.CASCADE)
    name = models.CharField(max_length = 60)

    def __str__(self):
        return str(self.name)

class Student(models.Model):
    name = models.CharField(max_length = 35)
    age = models.CharField(max_length = 10)
    birthdate = models.DateTimeField(null = True , blank = True )    
    college = models.ForeignKey(College, on_delete = models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)
