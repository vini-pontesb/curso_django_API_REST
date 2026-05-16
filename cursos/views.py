from rest_framework import generics, viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

# =========================== API V1 ============================

class CursosAPIView(generics.ListCreateAPIView): #endpoints de coleção
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView): #endpoints de indivíduos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView): #endpoints de coleção
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    #Sobrescrevendo o metodo get_queryset para que ele retorne apenas as avaliações de um curso específico
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            #Se houver curso_pk, retorna as avaliações de um curso específico
            return self.queryset.filter(curso_id=self.kwargs['curso_pk'])
        #Se não houver curso_pk, retorna todas as avaliações
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView): #endpoints de indivíduo
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    #Sobrescrevendo o metodo get_object para que ele retorne apenas as avaliações de um curso específico
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            #Se houver curso_pk, retorna a avaliação pelo curso_pk e pk
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs['curso_pk'], pk=self.kwargs['avaliacao_pk'])
        #Se não houver curso_pk, retorna a avaliação pelo pk
        return get_object_or_404(self.get_queryset(), pk=self.kwargs['avaliacao_pk'])

# =========================== API V2 ============================
class CursoViewSet (viewsets.ModelViewSet):
    # Viewsets de coleção e indíviduo, porém com menos codigo
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # Endpoint personalizado para obter as avaliações de um curso específico
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)

# VIEWSET PADRÃO:
'''class AvaliacaoViewSet (viewsets.ModelViewSet):
    # Viewsets de coleção e indíviduo, porém com menos codigo
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer'''

# VIEWSET CUSTOMIZADA PARA NÃO POSSIBILITAR O MÉTODO LIST (passa os métodos possíveis como parâmetro da função)
class AvaliacaoViewSet (mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer