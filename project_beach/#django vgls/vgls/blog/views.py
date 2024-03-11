from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post


######################
# Home Page Function #
######################
# This will handle the traffic from the home page of the blog
# Will handle a request function and then send the user to what they want to see
def home(request):
    # Here we have called the posts table from the database to show all of the blog posts that have been created.
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


######################################################################
# Class Based Views to Post Details,Create, Update, and Delete Views #
######################################################################
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    


#######################
# About Page Function #
#######################
# This will handle the traffic from the about page of the blog
# Will handle a request function and then send the user to what they want to see
def about(request):
    # For this, we have added a title to the about webpage which is in {}.
    return render(request, 'blog/about.html', {'title': 'About'})
