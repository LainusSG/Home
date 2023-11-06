from rest_framework import routers
from views import HomeView

router = routers.DefaultRouter()
router.register ('API/projects', HomeView, 'home')
urlpatterns = router.urls
