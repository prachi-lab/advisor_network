import csv

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required




def home(request):
	title = 'Welcome: This is the Home Page for Advisor Management'
	form='Welcome: This is the Home Page for Advisor Management'
	context = {
	  "title": title,
	   "test": form,
	}
	#return render(request, "home.html",context)
	return redirect('/list_of_advisor')
@login_required
def list_of_advisor(request):
	form = AdvisorSearchForm(request.POST or None)
	title = 'List of Advisor'
	queryset = Advisor.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
		"form" : form
	}
	if request.method == 'POST' :
		category = form['category'].value()
		queryset = Advisor.objects.filter(  # category__icontains=form['category'].value(),
			advisor_name__icontains=form['advisor_name'].value()
		)

		if (category != '') :
			queryset = queryset.filter(category_id=category)
	if request.method == 'POST' :

	  if form['export_to_CSV'].value() == True :
		  response = HttpResponse(content_type='text/csv')
		  response['Content-Disposition'] = 'attachment; filename="List of Advisors.csv"'
		  writer = csv.writer(response)
		  writer.writerow(['CATEGORY', 'ADVISOR NAME', 'ADVISOR ID','TOTAL QUANTITY'])
		  instance = queryset
		  for advisor in instance :
			  writer.writerow([advisor.category, advisor.advisor_name, advisor.advisor_id,advisor.total_quantity])
		  return response

	  context = {
		       "form" : form,
		       "title" : title,
		       "queryset" : queryset,
			}

	return render(request, "list_of_advisor.html", context)
@login_required
def add_advisor(request):
	form = AdvisorCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/list_of_advisor')
	context = {
		"form": form,
		"title": "Add ADVISOR",
	}
	return render(request, "add_advisor.html", context)
def update_advisor(request, pk):
	queryset = Advisor.objects.get(id=pk)
	form = AdvisorUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = AdvisorUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully Saved')
			return redirect('/list_of_advisor')

	context = {
		'form':form
	}
	return render(request, 'add_advisor.html', context)
def delete_advisor(request, pk):
	queryset = Advisor.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Deleted Successfully')
		return redirect('/list_of_advisor')
	context = {

	}
	return render(request, 'delete_advisor.html',context)

def advisor_detail(request, pk):
	queryset = Advisor.objects.get(id=pk)
	context = {
		"queryset": queryset,
	}
	return render(request, "advisor_detail.html", context)

@login_required
def list_of_advisor(request):
	form = AdvisorHistorySearchForm(request.POST or None)
	title = 'HISTORY DATA'
	queryset = AdvisorHistory.objects.all()

	context = {
		"title": title,
		"queryset": queryset,
		"form" : form,
	}


	if request.method == 'POST' :
		category = form['category'].value()
		queryset = AdvisorHistory.objects.filter(
			advisor_name__icontains=form['advisor_name'].value(),
			last_updated__range=[
				form['start_date'].value(),
				form['end_date'].value()
			]
		)
		if (category != '') :
			queryset = queryset.filter(category_id=category)

			if form['export_to_CSV'].value() == True :
				response = HttpResponse(content_type='text/csv')
				response['Content-Disposition'] = 'attachment; filename="Advisor History.csv"'
				writer = csv.writer(response)
				writer.writerow(
					['CATEGORY',
					 'ADVISOR NAME',
					 'ADVISOR ID'
					 'TOTAL QUANTITY',
					 'ISSUED ADVISOR',
					 'RECEIVED ADVISOR',
					 'RECEIVE BY',
					 'ISSUE BY',
					 'LAST UPDATED'])
				instance = queryset
				for advisor in instance :
					writer.writerow(
						[advisor.category,
						 advisor.advisor_name,
						 advisor.advisor_id,
						 advisor.total_quantity,
						 advisor.issued_advisor,
						 advisor.received_advisor,
						 advisor.receive_by,
						 advisor.issue_by,
						 advisor.last_updated])
				return response

		context = {
			"form" : form,
			"title" : title,
			"queryset" : queryset,
		}
	return render(request, "list_of_advisor.html",context)


