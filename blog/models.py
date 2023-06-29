from django.db import models
class New(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tittle
class Image(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return str(self.id)

