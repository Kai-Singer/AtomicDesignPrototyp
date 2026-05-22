from django.shortcuts import render
from ..utils import NAVBAR_ITEMS, SERVICES_LIST

### Home Seite ###
def home(request):
  return render(request, "pages/home.html", {
    "navbar_items": NAVBAR_ITEMS,
    "services_list": SERVICES_LIST,
  })

### Hilfe Seite ###
def help(request):
  return render(request, "pages/help.html", {
    "navbar_items": NAVBAR_ITEMS,
  })