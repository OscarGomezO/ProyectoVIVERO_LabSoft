#from anaconda_navigator.widgets.lists import content
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name': 'Viveros',
        'user': 'NAMENAME',
        #'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%N hrs'),
        'timestamp': datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        'picture': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fagriculturers.com%2Fla-tendencia-de-producir-arboles-en-viveros%2F&psig=AOvVaw3DKrP2k-gvhwKI09n4p7dB&ust=1618004903352000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLi3qo_Q7-8CFQAAAAAdAAAAABAD',
        #https://www.agroalimentando.com/mediaserver/4/main-10217.jpeg
    }
]

def list_posts(request):
    """"List existing posts"""
    #Posts = "Web Site VIVEROS."
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} -<i>{timestamp}</i></small></p>   
        <figure><img src="{picture}"/></figure>        
        """.format(**post))
    return HttpResponse('<br>'.join(content))


