from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import GoGame

def index(request):
    games = GoGame.objects.all()
    context = {'games': games}
    return render_to_response('index.html', context, RequestContext(request))

def games(request, game_id):
    game = GoGame.objects.get(id=game_id)
    context = {'game': game}
    return render_to_response('games.html', context, RequestContext(request))