from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=20)
	money = models.DecimalField(max_digits=6,decimal_places=2,default=0)
	FB = models.BigIntegerField(default=0)
	SW = models.BigIntegerField(default=0)
	HBC = models.BigIntegerField(default=0)
	WMT = models.BigIntegerField(default=0)

	def __str__(self):
		return self.name

class share(models.Model):
	user_id = models.ForeignKey('User')
	session_id = models.BigIntegerField(default=0)
	sequence_id = models.BigIntegerField(default=0)
	symbol = models.CharField(max_length=4)
	trans_time = models.CharField(max_length=20)
	_type = models.CharField(max_length=5)
	amount = models.PositiveSmallIntegerField(default=0)
	ex_price = models.DecimalField(max_digits=6,decimal_places=2,default=0)

	def __str__(self):
		return self.symbol