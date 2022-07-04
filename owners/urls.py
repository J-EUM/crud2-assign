from django.urls import path, include
from owners.views import DogsView, OwnersView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', OwnersView.as_view()),
    path('/dogs', DogsView.as_view())
]