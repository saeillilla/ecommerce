from django.urls import path
from products import views
urlpatterns = [


    path('addproduct/',views.addProduct),
    path('all_products/',views.all_products),
    path('viewproduct/<int:id>/',views.view_products ),
    path('addToWishList/<int:id>/',views.addWishlist ),
    path('removefromcart/<int:id>/',views.removeFromCart ),
    path('removeFromWishlist/<int:id>/',views.removeFromWishlist ),
    path('removeFromWishlist1/<int:id>/',views.removeFromWishlist1 ),

    path('addCart/<data>/',views.addCart),
    path('cart/',views.cart),
    path('sell_products/',views.myProducts),
    path('wishlist/',views.view_wishlist),
    path('checkout/',views.checkout),
    path('payment/',views.payment1),
    path('success' , views.success , name='success')






]
