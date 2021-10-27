from django.shortcuts import render
from .models import QrCode
# Create your views here.
def home(request):
   if request.method=="POST":
      Qrtxt=request.POST['qrtext']
      QrCode.objects.create(qrtxt=Qrtxt)

   qr_code=QrCode.objects.all()
   return render(request,"index.html",{'qr_code':qr_code})