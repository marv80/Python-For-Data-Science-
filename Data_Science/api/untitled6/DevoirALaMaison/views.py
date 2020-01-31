from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .models import Subject
from .serializers import SubjectSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("Here is the home page")

@csrf_exempt
def i_want_a_list(request):
    if request.method == "GET":
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        content = JSONParser().parse(request)
        serializer = SubjectSerializer(data = content)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def subject_detail(request, subject_id):
    try:
        subject = Subject.objects.get(IDSubject=subject_id)
    except Subject.DoesNotExist:
        return HttpResponse(str(subject_id), status=404)
    if request.method == "GET":
        serializer = SubjectSerializer(subject)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        # je recup le content du request et parse en JSON
        content = JSONParser().parse(request)
        # je serialise le JSON en instance de Subject
        serializer = SubjectSerializer(subject)
        serializer.update(subject, content)

        return JsonResponse(serializer.data, status=201)
    elif request.method == "DELETE":
        subject.delete()
        return HttpResponse("Suppression faite!", status=204)

def predict_activity(unscaled_data):
    import joblib
    colonnes        = ['IDSubject','AGE','SPORT','label','xchest','ychest','zchest','ecg','resp','xwrist','ywrist','zwrist','bvp','temp']
    path_to_model   = "../model_simple.sav"
    path_for_scaler = "../scaler.sav"
    unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]
    model           = joblib.load(path_to_model)
    scaler          = joblib.load(path_for_scaler)
    donnees_scalees = scaler.transform([unscaled_data])
    activity          = model.predict(donnees_scalees)
    return activity

@csrf_exempt
def predict(request):
    """
    Renvoie un subject avec l'activité completee
    (Attend une activity innexistante == null)
    """
    #if request.method == 'GET':
     #   return JsonResponse(serializer.errors, status=400)

    if request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = SubjectSerializer(data=data)
        if serializer.is_valid():
            data["activity"]        = predict_activity(data)
            serializer          = SubjectSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)
