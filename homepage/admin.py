from __future__ import unicode_literals

from django.contrib import admin
from .models import User, DegreeProgram, Office, Post

admin.site.register(User)
admin.site.register(DegreeProgram)
admin.site.register(Office)
admin.site.register(Post)

