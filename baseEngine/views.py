from django.shortcuts import redirect

def redirectBase(request):
	return redirect('professionsListUrl', permanent = True)