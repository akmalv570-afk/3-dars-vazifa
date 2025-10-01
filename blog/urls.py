from django.urls import path

from . import views
urlpatterns = [
    path("", views.index),
    path("sport/", views.sport),
    path("dasturlash/", views.dasturlash),
    path("posts/<int:post_id>", views.article)

]