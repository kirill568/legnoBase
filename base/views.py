from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import *
from .forms import *
from autoFillBase.fillingEngine import *

itemOnThePage = 10

def search(model, searchQuery):
	names = model.objects.filter(name__icontains = searchQuery)
	print(names)
	return names

def isAuth(request):
	if not request.user.is_authenticated and not request.user.is_staff:
		return False
	return True

def professionsList(request):
	title = 'legno base'
	return render(request, 'base/index.html', context={'title': title})

def designersList(request):
	searchQuery = request.GET.get('search', '')
	pageNumber = request.GET.get('page', 1)

	if searchQuery != '':
		names = search(Designers, searchQuery)
	else:
		names = Designers.objects.all()

	paginator = Paginator(names, itemOnThePage)
	page = paginator.get_page(pageNumber)
	isPaginated = page.has_other_pages()

	if page.has_previous():
		prevUrl = '?page={}'.format(page.previous_page_number())
	else:
		prevUrl = ''

	if page.has_next():
		nextUrl = '?page={}'.format(page.next_page_number())
	else:
		nextUrl = ''

	profession = 'designers'
	form = DesignersForm()
	return render(request, 'base/professions.html', context = {'page_object': page, 'isPaginated':isPaginated, 
															   'nextUrl': nextUrl, 'prevUrl': prevUrl,
															   'profession': profession, 'form': form})

def buildersList(request):
	searchQuery = request.GET.get('search', '')
	pageNumber = request.GET.get('page', 1)

	if searchQuery != '':
		names = search(Builders, searchQuery)
	else:
		names = Builders.objects.all()

	paginator = Paginator(names, itemOnThePage)
	page = paginator.get_page(pageNumber)
	isPaginated = page.has_other_pages()

	if page.has_previous():
		prevUrl = '?page={}'.format(page.previous_page_number())
	else:
		prevUrl = ''

	if page.has_next():
		nextUrl = '?page={}'.format(page.next_page_number())
	else:
		nextUrl = ''

	profession = 'builders'
	form = BuildersForm()
	return render(request, 'base/professions.html', context = {'page_object': page, 'isPaginated':isPaginated, 
															   'nextUrl': nextUrl, 'prevUrl': prevUrl,
															   'profession': profession, 'form': form})

def finishersList(request):
	searchQuery = request.GET.get('search', '')
	pageNumber = request.GET.get('page', 1)

	if searchQuery != '':
		names = search(Finishers, searchQuery)
	else:
		names = Finishers.objects.all()

	paginator = Paginator(names, itemOnThePage)
	page = paginator.get_page(pageNumber)
	isPaginated = page.has_other_pages()

	if page.has_previous():
		prevUrl = '?page={}'.format(page.previous_page_number())
	else:
		prevUrl = ''

	if page.has_next():
		nextUrl = '?page={}'.format(page.next_page_number())
	else:
		nextUrl = ''
		
	profession = 'finishers'
	form = FinishersForm()
	return render(request, 'base/professions.html', context = {'page_object': page, 'isPaginated':isPaginated, 
															   'nextUrl': nextUrl, 'prevUrl': prevUrl,
															   'profession': profession, 'form': form})

class DesignersCreate(View):
	def post(self, request):
		bound_form = DesignersForm(request.POST)
		profession = 'designers'
		names = Designers.objects.all()
		if bound_form.is_valid():
			newDesigner = bound_form.save()
			return redirect('designersListUrl')
		return render(request, 'base/professions.html', context = {'names': names, 'profession': profession, 'form': bound_form})

class BuildersCreate(View):
	def post(self, request):
		bound_form = BuildersForm(request.POST)
		profession = 'builders'
		names = Builders.objects.all()
		if bound_form.is_valid():
			newBuilders = bound_form.save()
			return redirect('buildersListUrl')
		return render(request, 'base/professions.html', context = {'names': names, 'profession': profession, 'form': bound_form})

class FinishersCreate(View):
	def post(self, request):
		bound_form = FinishersForm(request.POST)
		profession = 'finishers'
		names = Finishers.objects.all()
		if bound_form.is_valid():
			newFinishers = bound_form.save()
			return redirect('finishersListUrl')
		return render(request, 'base/professions.html', context = {'names': names, 'profession': profession, 'form': bound_form})

def designersDelete(request, name):
	if not isAuth(request):
		return HttpResponse('<h1>ERROR 403</h1>')

	designer = Designers.objects.get(name__iexact = name)
	designer.delete()
	return redirect('designersListUrl')

def finishersDelete(request, name):
	if not isAuth(request):
		return HttpResponse('<h1>ERROR 403</h1>')

	finisher = Finishers.objects.get(name__iexact = name)
	finisher.delete()
	return redirect('finishersListUrl')

def buildersDelete(request, name):
	if not isAuth(request):
		return HttpResponse('<h1>ERROR 403</h1>')

	builder = Builders.objects.get(name__iexact = name)
	builder.delete()
	return redirect('buildersListUrl')

def designersUpdate(request):
	if not isAuth(request):
		return HttpResponse('<h1>ERROR 403</h1>')

	entrys = [designer.name for designer in Designers.objects.all()]
	town = ["барнаул", "barnaul", "барнауле", "брн", "brn"]
	keyWords = ["дизайн интерьеров", "дизайн интерьера", 
			"дизайнер интерьеров", "дизайнер интерьера", 
			"дизайн помещений", "дизайн жилых и нежилых помещений", 
			"дизайн нежилых помещений", "дизайн жилых помещений"]

	finding = findEngine(entrys, town, keyWords)
	scanDesigners = finding.recursiveScan()
	findDesigners = finding.sortPeoples()
	for designer in findDesigners:
		try:
			Designers.objects.create(name = designer)
		except:
			print(designer)
	return(redirect('designersListUrl'))

def buildersUpdate(request):
	if not isAuth(request):
		return HttpResponse('<h1>ERROR 403</h1>')

	entrys = [builder.name for builder in Builders.objects.all()]
	town = ["барнаул", "barnaul", "барнауле", "брн", "brn"]
	keyWords = ["строительство", "стройка", "строительные"]

	finding = findEngine(entrys, town, keyWords)
	scanBuilders = finding.recursiveScan()
	findBuilders = finding.sortPeoples()
	for builder in findBuilders:
		try:
			Builders.objects.create(name = builder)
		except:
			print(builder)
	return(redirect('buildersListUrl'))

def finishersUpdate(request):
	if not isAuth(request):
		return HttpResponse('<h1>ERROR 403</h1>')

	entrys = [finisher.name for finisher in Finishers.objects.all()]
	town = ["барнаул", "barnaul", "барнауле", "брн", "brn"]
	keyWords = ["отделоч", "ремонт", "отделка"]

	finding = findEngine(entrys, town, keyWords)
	scanFinisher = finding.recursiveScan()
	findFinisher = finding.sortPeoples()
	for finisher in findFinisher:
		try:
			Finishers.objects.create(name = finisher)
		except:
			print(finisher)
	return(redirect('finishersListUrl')) 




