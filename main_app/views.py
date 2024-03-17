from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from main_app.services.placement import find_prediction
from main_app.services.score import score
import json
import pandas as pd

# Create your views here.

@api_view(["GET"])
def placement(request):
    try:
        prediction = find_prediction()
        return JsonResponse(prediction, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def analysis(request):
    try:
        input_request = request.body
        decode_input_request = input_request.decode('utf8').replace("'", '"')
        request_dict = json.loads(decode_input_request)
        email = request_dict['email']
        sem = request_dict['sem']
        find_score = score(input_id = email,sem_name = sem)
        print(find_score)
        return Response(find_score, status.HTTP_200_OK)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
