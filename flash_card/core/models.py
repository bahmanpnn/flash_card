from django.db import models
from django.contrib.auth import get_user_model



User=get_user_model()

class FlashCard(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
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

