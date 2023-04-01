from rest_framework.serializers import ModelSerializer
from core.models import FlashCard

class CreateFlashCardSerializer(ModelSerializer):
    class Meta:
        model=FlashCard
        # fields=("question","answer")
        fields="__all__"

class UpdateFlashCardSerializer(ModelSerializer):
    class Meta:
        model=FlashCard
        fields=("question","answer")
        # fields="__all__"

class ListFlashCardSerializer(ModelSerializer):
    class Meta:
        model=FlashCard
        fields="__all__"