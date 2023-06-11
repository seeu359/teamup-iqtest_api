from rest_framework import serializers

from .. import models
from ..services import domain
from . import mixins


class TestSerializer(serializers.Serializer):
    login = serializers.CharField()

    def validate_login(self, login: str) -> str | None:
        if domain.is_valid_login(login):
            return login
        raise serializers.ValidationError('Login should contain only letters and be 10 characters long')


class CreateTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Test
        fields = ('login',)


class CreateIQTestSerializer(mixins.LoginFieldMixin):

    class Meta:
        model = models.IQTest
        fields = ('login', 'result',)


class CreateEQTestSerializer(mixins.LoginFieldMixin):
    result = serializers.ListSerializer(child=serializers.CharField(max_length=5))

    class Meta:
        model = models.EQTest
        fields = ('login', 'result',)

    def validate_result(self, result: list):
        if domain.is_eq_valid_result(result):
            return result
        raise serializers.ValidationError('Result must contains 5 unique elements')
