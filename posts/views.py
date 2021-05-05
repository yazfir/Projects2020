""" Posts views """

#Django
#from django.http import HttpResponse
from django.shortcuts import render

#Utilities
from datetime import datetime


posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/237/200/200',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/84/200/200',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/784/200/200',
    }
]

def list_posts(request):
    """ List existing posts. """

    return render(request, 'feed.html', {'posts':posts})

#    content=[]
#    for post in posts:
#        content.append("""
#            <p><strong>{name}</strong></p>
#            <p><smal>{user} - <i>{timestamp}</i></small></p>
#            <figure><img src="{picture}"<figure>
#        """.format(**post))
#    return HttpResponse('<br>'.join(content))