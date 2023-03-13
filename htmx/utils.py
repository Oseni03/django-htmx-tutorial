from django.db.models import Max 
from .models import Film

def get_max_film():
  existing_films = Film.objects.all()
  if len(existing_films) < 1:
    return 0
  elif len(existing_films) == 1:
    return 1
  else:
    current_max = existing_films.aggregate(max_order=Max("order"))["max_order"]
    return current_max + 1


def reorder():
  existing_films = Film.objects.all()
  if len(existing_films) < 1:
    return
  film_list = existing_films.count()
  new_ordering = range(1, film_list+1)
  
  for order, film in zip(new_ordering, existing_films):
    film.order = order 
    film.save()