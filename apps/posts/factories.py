import factory

from .models import Post, Comment
from profiles.models import User
from django.contrib .webdesign import lorem_ipsum



class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    image = factory.django.ImageField(
        filename='example.jpg',
        wight=100,
        height=100,
        color='green',
        format='jpeg')

    @factory.lazy_attribute
    def user(self):
        return User.objects.get(id=1)

    @factory.post_generation
    def liked_users(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for liked_user in extracted:
                self.liked_users.add(liked_user)


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    @factory.lazy_attribute
    def user(self):
        return User.objects.all().order_by('?')[0]

    @factory.lazy_attribute
    def post(self):
        return Post.objects.all().order_by('?')[0]

    @factory.sequence
    def text(self):
        return lorem_ipsum.sentence()
