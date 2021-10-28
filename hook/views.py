from django.shortcuts import render
from django import template
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.conf import settings
from django.db.transaction import atomic, non_atomic_requests
from django.utils import timezone
from secrets import compare_digest
from .models import paystackreceive
# Create your views here.


# Create your views here.
@csrf_exempt
@require_POST
@non_atomic_requests
def hook(request):
    # return HttpResponse('Transaction successful')
    # if request.is_ajax():
    #     if request.method == 'POST':
    #         print (request.body)   
    #         return HttpResponse(request.body)
    # return HttpResponse('Okay')

    payload = json.loads(request.body)
    paystackreceive.objects.create(
        received_at=timezone.now(),
        payload=payload,
    )
    process_webhook_payload(payload)
    return HttpResponse("Message received okay.", content_type="text/plain")

@atomic
def process_webhook_payload(payload):
    # TODO: business logic
    ...
