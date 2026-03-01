from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

# As classes no plural servirão para os verbos HTTP (GET e POST) e as no singular para o restante do CRUD

class CusosAPIView(generics.ListCreateAPIView):
    # Métodos GET e POST
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CusoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    # Métodos GET e POST
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
