from django.contrib import admin

from .models import Advisor
from .models import *
from .forms import AdvisorCreateForm
class AdvisorCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'advisor_name', 'advisor_id']
   form = AdvisorCreateForm
   list_filter = ['category']
   search_fields = ['category', 'advisor_name']


admin.site.register(Advisor, AdvisorCreateAdmin)
