from django.conf.urls import url, include
from rest_framework import routers
from frank.rest_bo import views

router = routers.DefaultRouter()
router.register(r'skills', views.SkillViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'educations', views.EducationViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'interests', views.InterestViewSet)
router.register(r'travels', views.TravelViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]