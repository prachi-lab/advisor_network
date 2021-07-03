from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name

class Advisor(models.Model):
	category = models.CharField(max_length=50, blank=True, null=True)
	advisor_name = models.CharField(max_length=50, blank=True, null=True)
	advisor_id = models.IntegerField(default='0', blank=True, null=True)
	total_quantity = models.IntegerField(default='0', blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.advisor_name

class AdvisorHistory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
	advisor_name = models.CharField(max_length=50, blank=True, null=True)
	advisor_id = models.IntegerField(default='0', blank=True, null=True)
	total_quantity = models.IntegerField(default='0', blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)

	last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)


