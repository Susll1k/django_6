from django.shortcuts import render
from .models import Team, Player, Item

def home(request):
    
    teams = Team.objects.all()
    
    context = {
        'team' : teams
    }
    
    return render(request, 'home.html', {'team' : teams})

i = Item()
i.titles = 'Заголовок 1'
i.save()

titles = ['Заголовок 2', 'Заголовок 3', 'Заголовок 4']


for title in titles:
    i2 = Item()

    i2.titles = title
    i2.save()


items = Item.objects.all()

for item in range(1, len(items)+1):
    newitem = Item.objects.get(pk=item)


    newitem.titles = f"{newitem.titles}.id={newitem.id}"
    newitem.save(update_fields=['titles'])


for item in range(1, len(items)+1):
    if item%2:
        newitem = Item.objects.get(pk=item)


        newitem.delete()