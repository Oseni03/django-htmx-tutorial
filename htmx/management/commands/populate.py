import json
from django.conf import settings
from django.core.management.base import BaseCommand
from htmx.models import GDP, Languages 

class Command(BaseCommand):
  help = "Load Countries and languages"
  
  def handle(self, *args, **kwargs):
    if not GDP.objects.count():
      datafile = settings.BASE_DIR / "data" / "countries_data.json"
      with open(datafile, "r") as file:
        data = json.load(file)
      gdps = []
      lans = []
      for d in data:
        country = GDP.objects.create(
          name=d["name"],
          capital=d["capital"],
          population=d["population"],
          currency=d["currency"]
          )
        if d["languages"]:
          for lan in d["languages"]:
            lans.append(
              Languages.objects.create(
                name=lan,
                country=country)
            )
        gdps.append(country)
      GDP.objects.bulk_create(gdps)
      Languages.objects.bulk_create(lans)