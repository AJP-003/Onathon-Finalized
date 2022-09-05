from rest_framework import serializers
from multioption.models import ColorsModel

class Colorserializers(serializers.ModelSerializer):
    class Meta:
        model-ColorsModel
        fields="__all__"    