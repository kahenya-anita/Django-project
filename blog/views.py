from django.shortcuts import render

posts = [
    {
        'author': 'Anita',
        'title': 'Blog post 1',
        'content': 'First post',
        'date-posted': 'Aug 21, 2020'
    },
    {
        'author': 'Mary',
        'title': 'Blog post 2',
        'content': 'Second post',
        'date-posted': 'Aug 21, 2020'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    
