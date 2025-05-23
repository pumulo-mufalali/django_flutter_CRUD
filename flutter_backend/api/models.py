from django.db import models

class NoteModel(models.Model):
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[0:50]

    class Meta:
        ordering = ['-updated']