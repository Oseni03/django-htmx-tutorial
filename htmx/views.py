from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views import generic
from django.conf import settings
from django.db.models import Max 
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model

from .models import Film, Course, Modules, GDP, Languages
from .utils import get_max_film, reorder

# Create your views here.
class FilmListView(generic.ListView):
  model = Film
  paginate_by = 5
  context_object_name="films"
  
  def get_template_names(self):
    if self.request.htmx:
      return "htmx/partials/film_list_element.html"
    # super().get_template_names()
    return "htmx/listing.html"


def check_username(request):
  cred = {
    "username": "Oseni03", 
  }
  username = request.POST.get("username")
  #if get_user_model().objects.filter(username=username).exits()
  if username == cred["username"]:
    return HttpResponse("<div style='color: red;'>This user already exit</div>")
  else:
    return HttpResponse("<div style='color: green;'>This username is available</div>")


@require_http_methods(["POST"])
def add_film(request):
  name = request.POST.get("filmname")
  film = Film.objects.get_or_create(
    name=name,
    order=get_max_film())[0]
  messages.success(request, f"Added {film.name} to the list of film")
  return render(request, "htmx/partials/film_list.html", {"films": Film.objects.all()})


@require_http_methods(["DELETE"])
def delete_film(request, pk):
  film = get_object_or_404(Film, pk=pk)
  film.delete()
  reorder()
  return render(request, "htmx/partials/film_list.html", {"films": Film.objects.all()})


def search_film(request):
  search_word = request.POST.get("search")
  
  # Avengers will match avengers in the database
  results = Film.objects.filter(name__icontains=search_word)
  return render(request, "htmx/partials/search_result.html", {"results": results})


def clear(request):
  return HttpResponse("")


def sort(request):
  film_pks_order = request.POST.getlist("film_order")
  films = []
  filmlist = Films.objects.all()
  
  updated_films = []
  
  for idx, film_pk in enumerate(film_pks_order, start=1):
    # film = Film.objects.get(pk=film_pk)
    film = next(u for u in filmlist if u.pk==int(film_pk))
    
    if film.order != idx:
      film.order = idx 
      updated_films.append(film)
      
    films.append(film)
  Film.objects.bulk_update(updated_films, ["order"])
  paginator = Paginator(films, settings.PAGINATE_BY)
  page_number = len(film_pks_order) / settings.PAGINATE_BY
  page_obj = Paginator.get_page(page_number)
  return render(request, "htmx/partials/film_list.html", {"films": films})


def detail(request, pk):
  film = get_object_or_404(Film, pk=pk)
  context = {"film": film}
  return render(request, "htmx/partials/film_detail.html", context)


def upload_photo(request, pk):
  photo = request.FILES.get("photo")
  film = get_object_or_404(Film, pk=pk)
  film.photo.save(photo.name, photo)
  context = {"film": film}
  return render(request, "htmx/partials/film_detail.html", context)
  

def modules(request):
  course_pk = request.GET.get("course")
  print(course_pk)
  #course = get_object_or_404(Course, pk=course_pk)
  modules = Modules.objects.filter(course=course_pk)
  context = {"modules": modules}
  return render(request, "htmx/partials/modules.html", context)
