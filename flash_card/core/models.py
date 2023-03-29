from django.db import models

# Create your models here.
class FlashCard(models.Model):
    question=models.TextField()
    answer=models.TextField()
    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "flashcard"
        verbose_name_plural = "flashcards"

    def __str__(self):
        if len(self.question)>25:
            return f'{self.question[0:25]}...'
        else:
            return f'{self.question}'

