from rest_framework import routers
from .API import ProjectViewSet

router = routers.DefaultRouter()
router.register ('/projects', ProjectViewSet, 'projects')
urlpatterns = router.urls
