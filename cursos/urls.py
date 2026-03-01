from django.urls import path
from .views import AvaliacoesAPIView, CusosAPIView, AvaliacaoAPIView, CusoAPIView

urlpatterns = [
    path("cursos/", CusosAPIView.as_view(), name="cursos"),
    path("cursos/<int:pk>/", CusoAPIView.as_view(), name="curso"),
    path("avaliacoes/", AvaliacoesAPIView.as_view(), name="avaliacoes"),
    path("avaliacoes/<int:pk>/", AvaliacaoAPIView.as_view(), name="avaliacao")
]
