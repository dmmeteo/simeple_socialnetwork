from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view

from posts.views import PostViewSet
from users.views import UserViewSet

schema_view = get_swagger_view(title='Socialnetwork API v1')

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(router.urls)),
    path('docs/', schema_view),
    path('api/auth-token/', obtain_jwt_token),
    path('api/refresh-token/', refresh_jwt_token),

]
