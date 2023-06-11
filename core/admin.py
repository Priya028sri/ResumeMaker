from django.contrib import admin
from .models import Academic, Skill,User,Cv,Profile,Referee,Contact

model_list = [User, Skill,Cv,Academic,Profile,Referee,Contact]
admin.site.register(model_list)

