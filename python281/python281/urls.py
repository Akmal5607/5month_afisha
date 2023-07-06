from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static


from posts.views import MainPageCBV, PostsCBV, post_detail_view, post_create_view
from python281 import settings
from user.views import auth_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageCBV.as_view()),
    path('posts/', PostsCBV.as_view()),
    path('posts/create/', post_create_view),
    path('posts/<int:id>/', post_detail_view),

    path('users/auth/', auth_view),
    path('users/register/', register_view),
    path('users/logout/', logout_view),
    path('posts/page/', )



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(document_root=settings.STATIC_URL)

