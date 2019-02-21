from django.http import HttpResponse,JsonResponse
from .models import Todo
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
import json
import datetime


@csrf_exempt
def index(request):

	if(request.method == 'GET'):	
		alltodos = {}
		# for obj in Todo.objects.all():

		json_data = {}
		datalist = []
		for obj in Todo.objects.all():
			data = {}
			data['id']=obj.id;
			data['name']=obj.todo_text
			data['published date']=  str(obj.publish_time)    #datetime.datetime(obj.publish_time).timestamp()
			data['update date']= str(obj.update_time)       #datetime.datetime(obj.update_time).timestamp()
			datalist.append(data)
		json_data['data'] = datalist

		# print(json_data)
		return JsonResponse(json_data)	
		# 	data = {}
		# 	data['name']=obj.todo_text
		# 	data['published date']=  obj.publish_time.strftime('%s')    #datetime.datetime(obj.publish_time).timestamp()
		# 	data['update date']= obj.update_time.strftime('%s')       #datetime.datetime(obj.update_time).timestamp()
		# 	alltodos[str(obj.id)] = data

		# json_data = alltodos
		# # print(json_data)
		# return JsonResponse(json_data,safe=False)

	if(request.method == 'POST'):
		data = json.loads(request.body)
		obj = Todo(todo_text = data['todo_text'], publish_time = timezone.now(),update_time = timezone.now())

		# return HttpResponse(data['todo_text'])
		obj.save()
		temp = {}
		temp['id'] = str(obj.id)
		temp['name'] = str(obj.todo_text)
		temp['publish_time'] =  str(obj.publish_time )                  #str(datetime.datetime(obj.publish_time).timestamp())
		temp['update_time'] =  str(obj.update_time )		
		return JsonResponse(temp)


@csrf_exempt
def detail(request, todo_id):

	if(request.method == 'GET'):	
		if(Todo.objects.filter(pk= todo_id).count() == 0):
			return JsonResponse({ 'message':'No Records Found'}, status = 404)

		obj = Todo.objects.get(pk = todo_id)
		temp = {}
		temp['id'] = str(todo_id)
		temp['name'] = str(obj.todo_text)
		temp['publish_time'] =  obj.publish_time.strftime('%s')                  #str(datetime.datetime(obj.publish_time).timestamp())
		temp['update_time'] =  obj.update_time.strftime('%s') #   str(datetime.datetime(obj.update_time).timestamp())
	
		return JsonResponse(temp)

	if(request.method == 'PUT'):	
		if(Todo.objects.filter(pk= todo_id).count() == 0):
			return JsonResponse({ 'message':'No Record Found'}, status = 404)
		
		data = json.loads(request.body)
		Todo.objects.filter(id = todo_id).update(todo_text = data['todo_text'], update_time = timezone.now())
		obj = Todo.objects.get(id = todo_id)
		temp = {}
		temp['id'] = str(obj.id)
		temp['name'] = str(obj.todo_text)
		temp['publish_time'] =  str(obj.publish_time )                  #str(datetime.datetime(obj.publish_time).timestamp())
		temp['update_time'] =  str(obj.update_time )		
		return JsonResponse(temp)	

	if(request.method == 'DELETE'):

		if(Todo.objects.filter(pk= todo_id).count() == 0):
			return JsonResponse({ 'message':'No Records Found'}, status = 404)
		
		Todo.objects.filter(id = todo_id).delete()	

		
		return JsonResponse({'message':'deleted'}, status = 200)	


@csrf_exempt
def search(request):


	if(request.method != 'GET'):
		return JsonResponse({'status':'Bad Request', 'message':'Only POST requests allowed'}, status = 400)


	json_data = {}
	datalist =  []
	# if( Todo.objects.filter(todo_text__icontains = request.GET.get('txt').count() == 0)):
	# 	return JsonResponse({ 'message':'No Records Found'}, status = 204)

	for obj in Todo.objects.filter(todo_text__icontains = request.GET.get('q')):
		data = {}
		data['id']=obj.id
		data['name']=obj.todo_text
		data['publish_time']=  str(obj.publish_time)    #datetime.datetime(obj.publish_time).timestamp()
		data['update_time']= str(obj.update_time)       #datetime.datetime(obj.update_time).timestamp()
		datalist.append(data)

	json_data['data'] = datalist

	# json_data = temp
	# print(json_data)
	return JsonResponse(json_data,safe=False)


