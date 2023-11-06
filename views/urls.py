from rest_framework import routers
from HomeView import HomeView

router = routers.DefaultRouter()
router.register ('HomeView/views', HomeView.home, 'views')
urlpatterns = router.urls
