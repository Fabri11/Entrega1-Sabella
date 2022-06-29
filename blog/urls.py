
from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('',views.render_posts , name='posts'),
    path('<int:post_id>', views.detalles_post, name='detalles_post'),
    path('post_form', views.postForm, name='post_form')
]