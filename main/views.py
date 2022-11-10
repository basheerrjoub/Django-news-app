from django.shortcuts import render
from django.views import View
from .models import Post
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

# Create your views here.


class HomePage(View):

    template_name = "home.html"

    def get(self, request):
        latest_posts = Post.objects.all()
        paginator = Paginator(latest_posts, 6)
        page_number = request.GET.get("page", 1)
        try:
            posts = paginator.page(page_number)
        except:
            posts = paginator.page(paginator.num_pages)
        return render(
            request,
            self.template_name,
            {"latest_posts": posts, "p1": posts[0:3], "p2": posts[3:6]},
        )


class PostDetail(DetailView):
    model = Post
    template_name = "post-detail.html"
