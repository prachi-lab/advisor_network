from django import forms
from .models import Advisor,AdvisorHistory


class AdvisorCreateForm(forms.ModelForm):
   class Meta:
     model = Advisor
     fields = ['category', 'advisor_name', 'advisor_id','total_quantity']

   def clean_category(self) :
      category = self.cleaned_data.get('category')
      if not category :
         raise forms.ValidationError('This field is required')
      '''for instance in Stock.objects.all() :
          if instance.category == category :
              raise forms.ValidationError(str(category) + ' is already created')'''
      return category

   def clean_advisor_name(self) :
      advisor_name = self.cleaned_data.get('advisor_name')
      if not advisor_name :
         raise forms.ValidationError('This field is required')
      for instance in Advisor.objects.all() :
          if instance.advisor_name == advisor_name :
              raise forms.ValidationError(str(advisor_name) + ' is already created')
      return advisor_name

class AdvisorHistorySearchForm(forms.ModelForm) :
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta :
        model = AdvisorHistory
        fields = ['category', 'advisor_name', 'start_date', 'end_date']
class AdvisorSearchForm(forms.ModelForm) :
    export_to_CSV = forms.BooleanField(required=False)
    class Meta :
         model = Advisor
         fields = ['category', 'advisor_name']

class AdvisorUpdateForm(forms.ModelForm) :
    class Meta :
         model = Advisor
         fields = ['category', 'advisor_name','advisor_id', 'total_quantity']





