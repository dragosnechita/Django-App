from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    comment_1 = {'author': 'Jamie Fox', 'content': "D'Artagnan M0th3r7uck3r!", 'date': '2020-09-20 14:00'}
    comment_2 = {'author': 'Leo DiCaprio', 'content': 'Interesting', 'date': '2020-09-20 14:01'}
    blog_posts = {"blog_entries":
        [
        {'title': 'Knock Knock', 'content': 'Who is that?', 'author': 'Django', 'created': '2020-09-20', 'comments':
            [comment_1, comment_2], 'image': 'https://shorturl.at/gkqE1', 'old':False},
        {'title': 'My second blog post', 'content': 'Content for my second blog post', 'author': 'Django', 'comments': [],
         'created': '2020-08-20',
         'image': 'https://shorturl.at/gkqE1', 'old':True}
    ]
    }
    return render(request, 'base.html', blog_posts)