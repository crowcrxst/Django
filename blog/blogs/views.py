from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm


def index(request):
    """Домашняя страница приложения Blogs."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Создает новое сообщение блога."""
    if request.method != 'POST':
        # Данные не отправлялись. создается пустая форма.
        form = BlogForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, entry_id):
    """Редактирует уже существующую запись."""
    entry = BlogPost.objects.get(id=entry_id)
    post = BlogPost.objects.all()
    if entry.owner != request.user:
        raise Http404
    else:
        if request.method != 'POST':
            # Исходный запрос, форма заполняется данными текущей записи.
            form = BlogForm(instance=entry)
        else:
            # Отправка данных POST; обработать данные.
            form = BlogForm(instance=entry, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('blogs:index'))

    context = {'entry': entry, 'form': form}
    return render(request, 'blogs/edit_post.html', context)