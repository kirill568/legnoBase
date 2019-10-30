from django.db import models

class Designers(models.Model):
	name = models.CharField(max_length = 255, unique = True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']

class Builders(models.Model):
	name = models.CharField(max_length = 255, unique = True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']

class Finishers(models.Model):
	name = models.CharField(max_length = 255, unique = True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']