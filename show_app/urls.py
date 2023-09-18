from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('show/create', views.new_show),
    path('create_show', views.create_show),
    path('show/<int:show_id>', views.show_id),
    path('show/<int:show_id>/delete', views.delete_show),
    path('show/<int:show_id>/edit', views.edit_show),
    path('update_show/<int:show_id>', views.update_show)
]
