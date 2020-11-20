import csv

from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from shortener.models import Url
from shortener.serializers import UrlSerializer


class UrlListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()


class UrlShortener(APIView):
    def post(self, request, origin_uri):
        try:
            url = Url.objects.get(url=origin_uri)
        except:
            url = Url(url=origin_uri)
            url.save()

        short_url = url.short_url

        return Response(short_url)


class UrlView(APIView):
    def get(self, request, hash):
        try:
            url = Url.objects.get(url_hash=hash)
            url = url.url
        except Exception as e:
            print(e)
            content = {'error': 'No such url'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        return HttpResponseRedirect(url)


class UrlExport(APIView):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        writer = csv.writer(response)
        fields = Url.objects.all().values_list('url', 'short_url')

        for row in fields:
            writer.writerow(row)

        return response



