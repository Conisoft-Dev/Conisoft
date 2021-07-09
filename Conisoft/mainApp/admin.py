from django.contrib import admin
from .models import Project,Member,Service,Timeline

# Register your models here.
admin.site.register(Timeline)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Member)
