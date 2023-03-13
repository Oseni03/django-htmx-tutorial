from django.urls import path, include
from django.views import generic

from . import views
from .forms import RegisterForm
from .models import Film, Course


# app_name = "htmx"

urlpatterns = [
  path('', generic.TemplateView.as_view(
    template_name="htmx/home.html"), 
    name="home"),
  path('validation/', generic.FormView.as_view(
    template_name="htmx/validation.html",
    form_class=RegisterForm), 
    name="validation"),
  path('listing-creating/', views.FilmListView.as_view(), 
    name="listing"),
  path('to-load/', generic.TemplateView.as_view(
    template_name="htmx/click_to_load.html"), 
    name="click_to_load"),
  path('toggle-message/', generic.TemplateView.as_view(
    template_name="htmx/toggle_message.html"), 
    name="toggle_message"),
  path('lazy-loading/', generic.TemplateView.as_view(
    template_name="htmx/lazy_loading.html"), 
    name="lazy-loading"),
  path('courses/', generic.ListView.as_view(
    template_name="htmx/courses.html",
    model = Course,
    context_object_name="courses"), 
    name="courses"),
  path('page2/', generic.TemplateView.as_view(
    template_name="htmx/page2.html"), 
    name="page2"),
  path('alternate/', generic.TemplateView.as_view(
    template_name="htmx/alternate.html"),
    name="alternate"),
  path("add-film/", views.add_film, name="add_film"),
  path("delete-film/<int:pk>/", views.delete_film, name="delete-film"),
  path("search-film/", views.search_film, name="search-film"),
  path("clear/", views.clear, name="clear"),
  path("check-username/", views.check_username, name="check-username"),
  path("sort/", views.sort, name="sort"),
  path("detail/<int:pk>/", views.detail, name="detail"),
  path("upload-photo/<int:pk>", views.upload_photo, name="upload-photo"),
  path("modules/", views.modules, name="modules"),
]