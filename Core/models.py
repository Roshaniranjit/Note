from django.db import models

class Note(models.Model):
    name=models.CharField(max_length=10)
    description = models.TextField()
    
    
    def __str__(self) -> str:
        return self.name
