from django.urls import path
# from .views import UserCreateAPIView, ListTask, list_todo
from .views import UserCreateAPIView

urlpatterns = [
    # class based get view
    # path('list_task', ListTask.as_view()),
    #
    # # function based get view
    # path('list_todo', list_todo),

    path('users/create', UserCreateAPIView.as_view(), name='create')
]