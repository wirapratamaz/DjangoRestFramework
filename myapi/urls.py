# router for handling URLs in a Django application
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router is set up to use a view
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [ #variable is a list of URLs that the application should handle.
    #"include" function to include the URLs that the router has been set up to handle
    path('', include(router.urls)),
    #used to provide views for authentication and registration
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]