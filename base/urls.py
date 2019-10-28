from django.urls import path
from .views import *


urlpatterns = [
	path('', professionsList, name = 'professionsListUrl'),
	path('designers/', designersList, name = 'designersListUrl'),
	path('builders/', buildersList, name = 'buildersListUrl'),
	path('finishers/', finishersList, name = 'finishersListUrl'),
	path('designers/create/', DesignersCreate.as_view(), name = 'designersCreateUrl'),
	path('builders/create/', BuildersCreate.as_view(), name = 'buildersCreateUrl'),
	path('finishers/create/', FinishersCreate.as_view(), name = 'finishersCreateUrl'),
	path('designers/update/', designersUpdate, name = 'designersUpdateUrl'),
	path('builders/update/', buildersUpdate, name = 'buildersUpdateUrl'),
	path('finishers/update/', finishersUpdate, name = 'finishersUpdateUrl'),
	path('designers/<str:name>/delete/', designersDelete, name = 'designersDeleteUrl'),
	path('finishers/<str:name>/delete/', finishersDelete, name = 'finishersDeleteUrl'),
	path('builders/<str:name>/delete/', buildersDelete, name = 'buildersDeleteUrl')
]