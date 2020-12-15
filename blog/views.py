from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post ,category
from taggit.models import Tag
from django.db.models import Count
# Create your views here.



class postview(ListView):
    model=Post
    paginate_by = 3




class PostDetail(DetailView):
    model=Post

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resent_post"] = Post.objects.all()[:3]
        context["categroies"] = category.objects.all().annotate(post_count=Count('post_Category'))
        context["tags"] = Tag.objects.all()
        return context



