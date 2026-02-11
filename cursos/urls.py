from django.urls import path
from .views import AvaliacaoAPIView, CusoAPIView

urlpatterns = [
    path("cursos/", CusoAPIView.as_view(), name="cursos"),
    path("avaliacoes/", AvaliacaoAPIView.as_view(), name="avaliacoes")
]
