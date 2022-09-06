from rest_framework import serializers
from pookalam_images.models import ColorsModel

class Colorserializers(serializers.ModelSerializer):
    class Meta:
        model=ColorsModel
        fields="__all__"