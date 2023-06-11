from datetime import datetime

from rest_framework import generics
from rest_framework.response import Response

from .. import models
from . import mixins, serializers


class CreateTestApiView(generics.CreateAPIView):
    serializer_class = serializers.CreateTestSerializer


class CreateIQTestApiView(mixins.CreateMixin):
    serializer_class = serializers.CreateIQTestSerializer
    model = models.IQTest


class CreateEQTestApiView(mixins.CreateMixin):
    serializer_class = serializers.CreateEQTestSerializer
    model = models.EQTest


class RetrieveTestApiView(generics.GenericAPIView):
    test_list = ['iqtest', 'eqtest']
    created_at = None
    serializer_class = serializers.TestSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        qs = self.get_queryset()
        self.created_at = qs.first().created_at
        res = {
            'login': qs.first().login,
            'tests': {}
        }
        res['tests'].update(self.get_response(qs))

        return Response(res)

    def get_queryset(self):
        login = self.request.data.get('login')
        return models.Test.objects.filter(login=login).select_related('iqtest', 'eqtest')

    def get_response(self, qs) -> dict:
        res = {}

        for test in self.test_list:
            if qs.values(test).first()[test]:
                result = '{}__result'.format(test)
                completed_at = '{}__completed_at'.format(test)

                values = qs.values(result, completed_at).first()
                exc_time = self.get_exec_time(values[completed_at])

                res[test] = {'result': values[result], 'exc_time': exc_time}

        return res

    def get_exec_time(self, completed_at: datetime) -> str:
        created_at = self.created_at.replace(microsecond=0)
        return str(completed_at.replace(microsecond=0) - created_at)
