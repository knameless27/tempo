from .views import RoutineViewSet, RoutineTypeViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register("routines", RoutineViewSet, 'routines')
router.register("routine-types", RoutineTypeViewSet, 'routine_types')

urlpatterns = router.urls
