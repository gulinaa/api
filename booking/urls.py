from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from main.views import *
from order.views import OrderViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="BOOKING API",
      default_version='v1',
      description="My Booking site: StaySafe",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
# router.register('guesthouse', GuestHouseViewSet)
router.register('hotels', HotelViewSet)
router.register('comment', CommentViewSet)
router.register('likes', LikesViewSet)
router.register('rating', RatingViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', schema_view.with_ui()),
    path('account/', include('account.urls')),
    path('reserve/', include('reserve.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

