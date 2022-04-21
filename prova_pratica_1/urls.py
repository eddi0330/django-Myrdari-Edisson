from django.urls import path
from prova_pratica_1.views import view_b,view_c, listaMaterie, materie_detail


app_name="prova_pratica_1"
urlpatterns=[
    path('materie/', listaMaterie, name="lista-Materie"),
    path('materie/<int:pk>/', materie_detail, name="materie-Detail")
    #path('view_b',view_b, name='view_b'),
    #path('view_c',view_c, name='view_c'),
]