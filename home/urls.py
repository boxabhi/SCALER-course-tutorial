
from django.urls import path

from home.views import BlogView ,PublicBlog

urlpatterns = [
    path('' , PublicBlog.as_view()),
    path('blog/' , BlogView.as_view()),


]
