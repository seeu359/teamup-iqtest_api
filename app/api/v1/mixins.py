from django.db.models import Model
from django.forms import model_to_dict
from rest_framework import serializers, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .. import models
from ..services import domain


class LoginFieldMixin(serializers.ModelSerializer):
    login = serializers.CharField()

    def validate_login(self, login: str) -> str | None:
        if domain.is_valid_login(login):
            return login
        raise serializers.ValidationError('Login should contain only letters and be 10 characters long')


class CreateMixin(CreateAPIView):
    model: Model

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        test = models.Test.objects.get(login=serializer.validated_data.get('login'))
        iq_test = self.model.objects.create(
            test_id=test.id, result=serializer.validated_data.get('result')
        )

        return Response({**model_to_dict(iq_test)})

    def post(self, request, *args, **kwargs):
        login = request.data.get('login')

        if models.Test.objects.filter(login=login).exists():
            return self.create(request, *args, **kwargs)

        return Response('The test with this login was not found', status=status.HTTP_404_NOT_FOUND)
