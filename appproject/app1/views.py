from django.shortcuts import render
from models import Player


def index_page(request):

    # new_player = Player(name='jinja')
    # new_player.save()

    all_players = Player.objects.all()
    print(all_players)



    return render(request, 'index.html')
