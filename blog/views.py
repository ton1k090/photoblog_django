from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Photo, Testimonial, Biography, Post, Comment


class HomeView(ListView):
    model = Photo, Testimonial
    template_name = 'main/index.html'
    extra_context = {'title': 'Главная страница'}

    def get_queryset(self):
        q1 = Photo.objects.all()
        return q1[:9]

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['testimonial_objects'] = Testimonial.objects.all()
        context['biography'] = Biography.objects.get(id=1)
        context['post_list'] = Post.objects.all()
        return context


class BlogView(ListView):
    model = Post.objects.all()
    template_name = 'blog/blog.html'
    extra_context = {'title': 'Блог'}
    slug_field = 'url'

    def get_queryset(self):
        q2 = Post.objects.all()
        return q2

    def get_context_data(self, *args, **kwargs):
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context['post_list'] = Post.objects.all()
        context['comment_list'] = Comment.objects.all()
        return context


