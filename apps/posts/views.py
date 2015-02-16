from django.views.generic import ListView, FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden

from profiles.models import User
from .models import Post
from .forms import LikePostForm


class PostListView(ListView):
    model = Post


class LikeView(FormView):
    form_class = LikePostForm

    def  get_success_url(self):
         return reverse('posts:list')

    def form_valid(self, form):
         post = Post.objects.get(id=form_data['post_id'])
         user = User.objects.get(id=form_data['user_id'])
         if not self.request.user.is_authenticated() and self.request.user.id != user.id:
              return HttpResponseForbidden()
         post.like_trigger(user)
         return super(LikeView, self).form_valid(form)


post_list_view = PostListView.as_view()
like_view = LikeView.as_view()
