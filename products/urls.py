from django.urls import path
from products import views
urlpatterns = [


    path('addproduct/',views.addProduct),
    path('all_products/',views.all_products),
    path('viewproduct/<int:id>/',views.view_products ),
    path('addToWishList/<int:id>/',views.addWishlist ),
    path('removefromcart/<int:id>/',views.removeFromCart ),
    path('removeFromWishlist/<int:id>/',views.removeFromWishlist ),
    path('addCart/<data>/',views.addCart),
    path('cart/',views.cart),





]
