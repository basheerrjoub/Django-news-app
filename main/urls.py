from django.urls import path
from .views import HomePage, PostDetail
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", HomePage.as_view(), name="home-url"),
    path(
        "post/<int:year>/<int:month>/<int:day>/<slug:slug>",
        PostDetail.as_view(),
        name="post-detail",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
