from django.db import models

class Mission(models.Model):
    mission_title = models.CharField(max_length=200)
    mission_description = models.CharField(max_length=10000)
    create_date = models.DateTimeField()

class TestCase(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    test_case_title = models.CharField(max_length=200)
    