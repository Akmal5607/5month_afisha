from django.shortcuts import render, redirect
from django.views.generic import ListView

from posts.models import Post
from posts.forms import PostCreateForm
from posts.constants import PAGINATION_LIMIT


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


class MainPageCBV(ListView):
    model = Post
    template_name = 'layouts/index.html'


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        search = request.GET.get('search')

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        if search:
            posts = posts.filter(title__contains=search)

        context = {
            'posts': posts,
            'user': request.user,
            'pages': range(1, max_page)
        }

        return render(request, 'posts/posts.html', context=context)


class PostsCBV(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'posts/posts.html'


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comment_set.all()
        }

        return render(request, 'posts/detail.html', context=context)


def post_create_view(request):
    if request.method == 'GET':
        context = {
            'form': PostCreateForm
        }

        return render(request, 'posts/create.html', context=context)

    if request.method == 'POST':
        data, files, = request.POST, request.FILES
        form = PostCreateForm(data, files)

        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate')
            )
            return redirect('/posts')

        return render(request, 'posts/create.html', context={
            'form': form
        })
