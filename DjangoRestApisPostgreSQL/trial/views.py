from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
 
from trial.models import Trial
from trial.serializer import TrialSerializer
from rest_framework.decorators import api_view
    
 
    
@api_view(['GET', 'POST', 'DELETE'])
def trial_list(request):
    if request.method == 'GET':
        trials = Trial.objects.all()
        email = request.GET.get('email', None)
        if email is not None:
            trials = trial.filter(email__icontains=email)
            hello(trials_serializer.data)
            
        trial_serializer = TrialSerializer(trials, many=True)
        hello(trial_serializer.data)
        return JsonResponse(trial_serializer.data, safe=False)
        
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        trial_data = JSONParser().parse(request)
        trial_serializer = TrialSerializer(data=trial_data)
    if trial_serializer.is_valid():
        trial_serializer.save()
        return JsonResponse(trial_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(trial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
@api_view(['GET', 'PUT', 'DELETE'])
def trial_detail(request, pk):
            # ... tutorial = Tutorial.objects.get(pk=pk)
    if request.method == 'GET':
        trial_serializer = TrialSerializer(trial)
        return JsonResponse(trial_serializer.data)
        hello()
    # ... tutorial = Tutorial.objects.get(pk=pk)
       # ...
    elif request.method == 'PUT':
        trial_data = JSONParser().parse(request)
        trial_serializer = TrialSerializer(trial, data=trial_data)
        if trial_serializer.is_valid():
            trial_serializer.save()
            return JsonResponse(trial_serializer.data)
            return JsonResponse(trial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            trial.delete()
            return JsonResponse({'message': 'Trial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'DELETE':
            count = Trial.objects.all().delete()
            return JsonResponse({'message': '{} Trial were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def trial_list_published(request):
    trials = Trial.objects.filter(published=True)
        
    if request.method == 'GET':
        trials_serializer = TrialSerializer(trials, many=True)
        print(trials_serializer.data)
        return JsonResponse(trials_serializer.data, safe=False)
    



def hello(t):
    print(t)
    
    

