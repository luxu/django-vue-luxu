from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, Sentenciado, Pavilhao
from .serializers import MessageSerializer, SentenciadoSerializer, PavilhaoSerializer

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class SentenciadoViewSet(viewsets.ModelViewSet):

    queryset = Sentenciado.objects.all()
    serializer_class = SentenciadoSerializer


class PavilhaoViewSet(viewsets.ModelViewSet):

    queryset = Pavilhao.objects.all()
    serializer_class = PavilhaoSerializer

