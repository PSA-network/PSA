"""
Definition of views.
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db import models
from .models import Blog
from .models import Comment # использование модели комментариев
from .models import News
from .forms import CommentForm # использование формы ввода комментария
from .forms import blogForm


def home(request):
    """Renders the home page."""
    newsBlockPosts = News.objects.order_by('-posted')[0:3] # запрос на выбор трёх первых новостей, отсортированных по дате (сначала последние)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'newsBlockPosts': newsBlockPosts,
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О Нашей Компании',
            #'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def links (request):
     """Renders the contact page."""
     assert isinstance(request, HttpRequest)
     return render(
            request,
            'app/links.html',
        {
            'title':'links',
            'message':'Your links page.',
            'year':datetime.now().year,
        }
    )
def registration(request):
 """Renders the registration page."""

 if request.method == "POST": # после отправки формы
    regform = UserCreationForm(request.POST)
    if regform.is_valid(): #валидация полей формы
      reg_f = regform.save(commit=False) # не сохраняем данные формы
      reg_f.is_staff = False # запрещен вход в административный раздел
      reg_f.is_active = True # активный пользователь
      reg_f.is_superuser = False # не является суперпользователем
      reg_f.date_joined = datetime.now() # дата регистрации
      reg_f.last_login = datetime.now() # дата последней авторизации

      reg_f.save() # сохраняем изменения после добавления данных(добавление пользователя в БД пользователей)

      return redirect('home') # переадресация на главную страницу послерегистрации
 else:
      regform = UserCreationForm() # создание объекта формы для вводаданных нового пользователя

 assert isinstance(request, HttpRequest)
 return render(
 request,
 'app/registration.html',
 {

 'regform': regform, # передача формы в шаблон веб-страницы

 'year':datetime.now().year,
 }
 )
def blog(request):
   """Renders the blog page."""
   posts = Blog.objects.order_by('-posted') # запрос на выбор всех статей из модели,отсортированных по убыванию даты опубликования

   assert isinstance(request, HttpRequest)
   return render(request,
      'app/blog.html',{         # параметр в {} – данные для использования в шаблоне.
           'title':'Блог',
           'posts': posts,             # передача списка статей в шаблон веб-страницы
           'year':datetime.now().year,
     }
 )
def blogpost(request, parametr):
 """Renders the blogpost page."""
 post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи попараметру
 comments = Comment.objects.filter(post=parametr)
 if request.method == "POST": # после отправки данных формы насервер методом POST:::запрос на вывод всех комментариев к конкретной статье
  form = CommentForm(request.POST) 
  if form.is_valid():
    comment_f = form.save(commit=False)
    comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованногопользователя
    comment_f.date = datetime.now() # добавляем в модельКомментария (Comment) текущую дату
    comment_f.post = Blog.objects.get(id=parametr) # добавляем в модельКомментария (Comment) статью, для которой данный комментарий
    comment_f.save() # сохраняем изменения после добавленияполей

    return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария
 else:
    form = CommentForm() # создание формы для ввода комментария
 assert isinstance(request, HttpRequest)
 return render(
     request,
 'app/blogpost.html',
 {
 'post_1': post_1, # передача конкретной статьи в шаблон вебстраницы
 'year':datetime.now().year,
 'comments': comments, # передача всех комментариев к данной статье в шаблон вебстраницы
'form': form, # передача формы в шаблон веб-страницы 
 }
 )
def services (request):
     """Renders the contact page."""
     assert isinstance(request, HttpRequest)
     return render(
            request,
            'app/services.html',
        {
            'title':'links',
            'message':'Your links page.',
            'year':datetime.now().year,
        }
    )

def newpost(request):     
    """Renders the blogpost page.""" 
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = blogForm(request.POST, request.FILES)  
        if form.is_valid():
            blog_f = form.save(commit=False)
            blog_f.date = datetime.now() # добавляем в модель текущую дату
            blog_f.save() # сохраняем изменения после добавления полей
            return redirect('blog') # переадресация
    else:
        form = blogForm() # создание формы для ввода
        assert isinstance(request, HttpRequest)     
        return render(        
        request, 
            'app/newpost.html', 
            {                                               
                'year':datetime.now().year, 
                'form': form, # передача формы в шаблон веб-страницы                
            }
        ) 

def news(request):
   """Renders the blog page."""
   posts = News.objects.order_by('-posted') # запрос на выбор всех статей из модели,отсортированных по убыванию даты опубликования

   assert isinstance(request, HttpRequest)
   return render(request,
      'app/news.html',{         # параметр в {} – данные для использования в шаблоне.
           'title':'Новости',
           'posts': posts,             # передача списка статей в шаблон веб-страницы
           'year':datetime.now().year,
     }
 )
def newspost(request, parametr):
# """Renders the blogpost page."""
    post_1 = News.objects.get(id=parametr) # запрос на выбор конкретной статьи попараметру

#    assert isinstance(request, HttpRequest)
    return render(request,
        'app/newspost.html',{
            'post_1': post_1, # передача конкретной статьи в шаблон вебстраницы
            'year':datetime.now().year,
         }
    )

@login_required
def orders(request):
   #if request.
   posts = News.objects.order_by('-posted') # запрос на выбор всех статей из модели,отсортированных по убыванию даты опубликования

   assert isinstance(request, HttpRequest)
   return render(request,
      'app/news.html',{         # параметр в {} – данные для использования в шаблоне.
           'title':'Новости',
           'posts': posts,             # передача списка статей в шаблон веб-страницы
           'year':datetime.now().year,
     }
 )
