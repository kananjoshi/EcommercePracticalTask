from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(r'',views.index,name='index' ),
    path(r'<int:id>', views.detail_view,name='detail_view'),
    path(r'add_product/',views.add_product, name='add_product'),
    path(r'login/', auth_views.login, name='login'),
    path(r'logout/', auth_views.logout, name='logout'),
    path(r'cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path(r'show_cart/',views.show_cart,name="show_cart"),
    path(r'place_order/',views.place_order,name="place_order"),
    path(r'api/v1/addporduct/',views.addporduct,name='addporduct')
 
]
