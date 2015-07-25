from django.contrib.auth.decorators import login_required
import mailchimp

from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import GoGame, GoUser

def index(request):
    error = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            GoUser.objects.create_user(email, email, password)
            user = authenticate(username=email, password=password)
            login(request, user)
            m = mailchimp.Mailchimp('22d12387b2447552b61abd6dc2b441e1-us9')
            try:
                m.lists.subscribe('cb60a9e4bb', {'email': email}, double_optin=False)
                error = None
            except mailchimp.Error as e:
                error = str(e)
            send_mail(
                'New sign up to GoGameReview - {}'.format(email),
                'And Mailchimp too!' if not error else 'Damn: {}'.format(error),
                'hello@gogamereview.com',
                ['drakethomas33@gmail.com'],
                fail_silently=False
            )
            return HttpResponseRedirect('/thanks/')
        except IntegrityError:
            error = 'Oops! This email address is already registered.'

    games = GoGame.objects.all()
    context = {
        'games': games,
        'error': error
    }
    return render_to_response('index.html', context, RequestContext(request))


@login_required
def thanks(request):
    return render_to_response('thanks.html', {}, RequestContext(request))


def games(request, game_id):
    game = GoGame.objects.get(id=game_id)
    context = {'game': game}
    return render_to_response('games.html', context, RequestContext(request))