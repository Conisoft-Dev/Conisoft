from django.contrib import admin
from .models import (
    Workshop,
    User,
    Edition,
    Course,
    PaperRequirement,
    Topic,
    Carosel,
    # Attendee
    )

# Register your models here.
admin.site.register(Workshop)
admin.site.register(User)
admin.site.register(Edition)
admin.site.register(Course)
admin.site.register(PaperRequirement)
admin.site.register(Topic)
admin.site.register(Carosel)
# admin.site.register(Attendee)

