from django.contrib import admin
from . models import Voter,Election,Candidate,Vote

# Register your models here.


admin.site.register(Voter)
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Vote)
