from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json

from .models import Session


# ---------- helper ----------
def get_session():
    obj, created = Session.objects.get_or_create(id=1)
    return obj


# ---------- frontend pages ----------
def mobile1(request):
    return render(request, "timerapp/mobile1.html")

def mobile2(request):
    return render(request, "timerapp/mobile2.html")


# ---------- backend logic ----------
def store_code(request):
    code = request.GET.get("code")
    s = get_session()
    s.code = code
    s.verified = False
    s.last_ping = None
    s.save()
    return JsonResponse({"status": "stored"})


@csrf_exempt
def verify_code(request):
    if request.method != "POST":
        return JsonResponse({"status": "invalid request"})

    data = json.loads(request.body)
    s = get_session()

    if str(s.code) == str(data.get("code")):
        return JsonResponse({"status": "verified"})
        s.verified = True
        s.last_ping = timezone.now()
        s.save()
        

    return JsonResponse({"status": "invalid"})


def ping(request):
    s = get_session()
    s.last_ping = timezone.now()
    s.save()
    return JsonResponse({"alive": True})


def status(request):
    s = get_session()

    if s.last_ping:
        diff = (timezone.now() - s.last_ping).seconds
        if diff > 10:  # mobile-2 closed
            s.verified = False
            s.save()

    return JsonResponse({"verified": s.verified})



