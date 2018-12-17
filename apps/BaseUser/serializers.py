# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import BaseUser


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = '__all__'



