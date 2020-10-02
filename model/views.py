from django.shortcuts import render
from .models import Model_3d
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import HttpResponse, Http404
import os


def index(request):
    model = Model_3d.objects.all()

    if request.method == 'POST':
        card_number = request.POST['card_number']
        email = request.POST['email']
        url = request.POST['url']
        url = '<a href="http://localhost:8000' + url + '" download="http://localhost:8000'+ url + '">Yuklash</a>'
        message = 'Hizmatimizdan foydalanganingiz uchun sizdan minnatdormiz. Modelni yuklab olish u.n quyidagi havolani bosing.\n' + url
        msg = EmailMultiAlternatives('Model', message, 'rahmetruslanov6797@gmail.com', [email])
        msg.attach_alternative(url, "text/html")
        msg.send()

    return render(request, "index.html", {'models':model})


def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/model")
            response['Content-Disposition']='inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404