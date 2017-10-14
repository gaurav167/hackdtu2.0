from django.shortcuts import render
from .blockch import blockch
from .models import User
import pandas as pd
from .associationruleminingapriori import check


def buys(request):
	if len(request.GET) != 0:
		return render(request,'mk_blockchain/success.html')
	check(1)
	return render(request,'mk_blockchain/buys.html',{})


def sells(request):
	if len(request.GET) != 0:
		return render(request,'mk_blockchain/malacious.html')
	check(0)
	return render(request,'mk_blockchain/sells.html',{})


def index(request):
	#chain = blockch.start()
	user = User.objects.filter(name='Minkush')
	return render(request,'mk_blockchain/index.html',{"User":user})

def sell(request):
	decrease = request.GET.get('decrease')
	_type = request.GET.get('type')
	if check(0) == 0:
		return render(request,'mk_blockchain/malacious.html')
	return render(request,'mk_blockchain/malacious.html')
	state = blockch.state	
	txnbuffer.append(blockch.makeTransaction(_type,decrease,'Minkush',state))
	if len(txnbuffer) == 5:
		chain = blockch.chain
		blockch.buffer_to_block(txnbuffer,chain)

def buy(request):
	increase = request.GET.get('increase')
	_type = request.GET.get('type')
	return render(request,'mk_blockchain/success.html')
	state = blockch.state
	txnbuffer.append(blockch.makeTransaction(_type,increase,'Minkush',state))
	if len(txnbuffer) == 5:
		chain = blockch.chain
		blockch.buffer_to_block(txnbuffer,chain)

def addMoney(request):
	increase = request.GET.get('increase')
	# user = User.objects.filter(name='Minkush')
	# user.money += increase
	# user.save()

def login(request):
	return render(request,'mk_blockchain/login.html')

def auth(request):
	user = User.objects.filter(name='Minkush')
	return render(request,'mk_blockchain/index.html',{"User":user})