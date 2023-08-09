from django.urls import path
from ExchangeLogistics.exchange.api.views import ViewDetailsDeleteUserProfileApiView, ProfileDetailsApiView
from ExchangeLogistics.accounts.api.views import CreateUserApiView, UpdateUserProfileApiView, LoginUserApiView

urlpatterns = [
    path('register/', CreateUserApiView.as_view(), name='api_register'),
    path('<int:pk>/profile/', UpdateUserProfileApiView.as_view(), name='api_update_profile'),
    path('<int:pk>/profile/', ViewDetailsDeleteUserProfileApiView.as_view(), name='api_view_delete_profile'),
    path('<int:pk>/profile/', ProfileDetailsApiView.as_view(), name='api_profile_details'),

    path('login/', LoginUserApiView.as_view(), name='api_login'),
]
