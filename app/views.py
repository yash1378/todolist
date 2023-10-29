from django.shortcuts import render
from django.http import HttpResponse
from  django.template import loader
from .models import Task
from django.utils import timezone
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Use this decorator if you want to disable CSRF protection for this view (for simplicity)
def receive_data(request):
    if request.method == 'POST':
        try:
            # Assuming the data is sent as JSON
            print(request.body)
            data = json.loads(request.body)
            print(data)
            instance = Task(task_text=data['task'], pub_date=data['pubDate'])
            instance.save()
            
            # Process the data as needed
            # In this example, we just display it
            
            return JsonResponse({'message': 'Data received on the server', 'data': data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    elif request.method == 'PUT':
      try:
        # Assuming the data is sent as JSON
        print(request.body)
        data = json.loads(request.body)
        tasks = Task.objects.get(task_text=data['task'])
        print(data)
        tasks.comp_date=timezone.now()
        tasks.save()
        
        # Process the data as needed
        # In this example, we just display it
        
        return JsonResponse({'message': 'Data received on the server', 'data': data}, status=200)
      except json.JSONDecodeError:
          return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed'}, status=405)



def main(request):
    tasks = Task.objects.all()
    data = [{"task": task.task_text, "pubDate": task.pub_date, "compDate": task.comp_date} for task in tasks]
    return JsonResponse(data, safe=False)


#Generic View
# from django.http import JsonResponse
# from django.views.generic import View
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# import json
# from .models import Task
# from django.utils import timezone

# @method_decorator(csrf_exempt, name='dispatch')
# class ReceiveDataView(View):
#     def post(self, request):
#         try:
#             # Assuming the data is sent as JSON
#             data = json.loads(request.body)
#             instance = Task(task_text=data['task'], pub_date=data['pubDate'])
#             instance.save()
#             return JsonResponse({'message': 'Data received on the server', 'data': data}, status=200)
#         except json.JSONDecodeError:
#             return JsonResponse({'message': 'Invalid JSON data'}, status=400)

#     def put(self, request):
#         try:
#             # Assuming the data is sent as JSON
#             data = json.loads(request.body)
#             task = Task.objects.get(task_text=data['task'])
#             task.comp_date = timezone.now()
#             task.save()
#             return JsonResponse({'message': 'Data received on the server', 'data': data}, status=200)
#         except json.JSONDecodeError:
#             return JsonResponse({'message': 'Invalid JSON data'}, status=400)

# @method_decorator(csrf_exempt, name='dispatch')
# class MainView(View):
#     def get(self, request):
#         tasks = Task.objects.all()
#         data = [{"task": task.task_text, "pubDate": task.pub_date, "compDate": task.comp_date} for task in tasks]
#         return JsonResponse(data, safe=False)

