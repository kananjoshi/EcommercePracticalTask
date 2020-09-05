from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index' ),
    path('<id>', views.detail_view,name='detail_view'),
]
