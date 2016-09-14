# from django.http import HttpResponse
from django.shortcuts import render
from .models import Treasure

# Create your views here.
def index(request):
  # name = 'Gold Nugget'
  # value = 1000.00
  # context = {
  #   'treasure_name': name,
  #   'treasure_val': value
  # }

  # return HttpResponse('<h1>Hello Explorers!</h1>')
  # return render(request, 'index.html', context)

  treasures = Treasure.objects.all()
  return render(request, 'index.html', {'treasures': treasures})

'''
class Treasure:
  def __init__(self, name, value, material, location, img_url):
    self.name = name
    self.value = value
    self.material = material
    self.location = location
    self.img_url = img_url

treasures = [
  Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM",
    'example.com/nugget.jpg'),
  Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO",
    'example.com/fools-gold.jpg'),
  Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA',
    'example.com/coffe-can.jpg')
]
'''