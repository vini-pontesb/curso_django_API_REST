from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursosAPIView(generics.ListCreateAPIView): #endpoints de coleção
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView): #endpoints de indivíduos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView): #endpoints de coleção
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView): #endpoints de indivíduo
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer