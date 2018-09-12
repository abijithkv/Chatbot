from rest_framework import serializers
from tgpi.models import Greet
from tgpi.models import Resp


class gr_serializer(serializers.ModelSerializer):
    class Meta:
        model = Greet
        fields = '__all__'


class rp_serializer(serializers.ModelSerializer):
    class Meta:
        model = Resp
        fields = '__all__'
