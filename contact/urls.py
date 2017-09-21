from django.conf.urls import include, url
from contact import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("contact", views.ContactViewSet)
router.register("contacttype", views.ContactTypeViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]