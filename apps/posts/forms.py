from django import forms

from profiles.models import User
from .models import Post


class LikePostForm(forms.Form):
    post_id = forms.CharField()
    user_id = forms.CharField()

    def clean_post_id(self):
        post_id = self.cleaned_data.get('post_id')
        return Post_object.filter(id=post_id).exists()

    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        return User_object.filter(id=user_id).exists()
