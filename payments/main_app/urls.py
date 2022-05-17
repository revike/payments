from django.urls import path
from main_app import views as main_app

app_name = 'main_app'

urlpatterns = [
    path('item/', main_app.ItemListView.as_view(), name='items'),
    path('item/<int:pk>/', main_app.ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>/', main_app.BuyView.as_view(), name='buy'),
    path('success/', main_app.SuccessView.as_view(), name='success'),
    path('cancel/', main_app.CancelView.as_view(), name='cancel'),
]
