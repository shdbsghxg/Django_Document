from django.contrib import admin

from .models import (
    # basic
    Topping, Pizza,
    # intermediate
    PostLike, User, Post,
    # self
    FacebookUser,
    # symmetrical
    InstagramUser,
)

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)

