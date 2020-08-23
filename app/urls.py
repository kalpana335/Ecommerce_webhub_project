from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name="login"),
    path('karma_login/',views.karma_login,name="karma_login"),
    path('signup/',views.signup,name="signup"),
    path('register/',views.register,name="register"),
    path('product_upload/',views.product_upload,name='product_upload'),
    path('add_product/',views.add_product,name='add_product'),
    # path('show_product/',views.show_product,name='show_product'),
    # path('pro/',views.pro,name='pro'),
    path('blog/',views.blog,name="blog"),
    path('cart/',views.cart,name="cart"),
    path('category/',views.category,name="category"),
    path('checkout/',views.checkout,name="checkout"),
    path('confirmation/',views.confirmation,name="confirmation"),
    path('elements/',views.elements,name="elements"),
    path('single_blog/',views.single_blog,name="single_blog"),
    path('tracking/',views.tracking,name="tracking"),
    path('single_product/',views.single_product,name="single_product"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
