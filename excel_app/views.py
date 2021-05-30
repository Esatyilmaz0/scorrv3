from excel_app.forms import SignupForm
from django.http.response import JsonResponse
import pandas
from excel_app.models import Log, Rapor, RaporGirdiler
from django.shortcuts import redirect, render
from .Scor_V5 import rapor_calistir_
from verify_email.email_handler import send_verification_email
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/hakkimizda.html")

def contact(request):
    return render(request, "home/iletisim.html")

def raporlariGetir(request):
    saha_no = request.GET.get("saha_no")
    raporlar = Rapor.objects.filter(saha_no=saha_no)
    return render(request, "create_raporlar.html", {"data":raporlar})
    
def rapor_getir(request):
    rapor_id = request.GET.get("rapor_id")
    
    girdiler = Rapor.objects.get(id=rapor_id).rapor.all()
    return render(request, "girdiler.html", {"data":girdiler})

def updateAciklama(request):
    girdi_id = request.GET["girdi_id"]
    girdi = RaporGirdiler.objects.get(id=girdi_id)
    girdi.aciklama = request.GET["aciklama"]
    girdi.save()
    log = Log(user=request.user)

    log.description = f"{request.user} Adlı Kullanıcı {girdi.saha_no} Saha No ve {girdi.saha_kod} Saha Kodlu {girdi_id} Id'sine Sahip Girdinin Açıklamasını {girdi.aciklama} Şeklinde Değiştirdi."
    log.saha_no = girdi.saha_no
    log.saha_kod = girdi.saha_kod
    log.save()

    return JsonResponse({"Msg":"Success"})


def uploadHamVeri(request):
    if request.method == "POST" and request.FILES['excelFile']:
        my_file = request.FILES["excelFile"]
        fs = FileSystemStorage(location=settings.MEDIA_ROOT) #defaults to   MEDIA_ROOT  
        filename = fs.save(my_file.name, my_file)

        ham_veri = pandas.read_excel(settings.MEDIA_ROOT +"\\" +  filename, engine="openpyxl")
        saha_no = ham_veri["Saha No"][0]
        sorgu_list = pandas.read_excel(settings.MEDIA_ROOT +"\\" +  "Sorgu_List.xlsx", engine="openpyxl")
        sorgu_ref = pandas.read_excel(settings.MEDIA_ROOT +"\\" +  "Sorgu_Ref.xlsx", engine="openpyxl")
            
        rapor = Rapor(user=request.user, saha_no=saha_no)
        rapor.save()
        
        girdiler = rapor_calistir_(ham_veri, sorgu_list, sorgu_ref, saha_no=saha_no, rapor=rapor)
        
        log = Log(user=request.user, saha_no=saha_no, saha_kod="")
        log.description = f"{request.user} Adlı KUllanıcı {saha_no} Kodlu Saha No'nun Rapor Girdilerini Oluşturdu."
        log.save()
        fs.delete(filename)
        return render(request, "raporlar.html", {"data":girdiler})
    return render(request, "raporlar.html")
            
# Sign Up View

class SignUpView(CreateView):
    form_class = SignupForm
    success_url = "/"
    template_name = 'register.html'
    def form_valid(self, form):
        username, password, email = form.cleaned_data.get('username'), form.cleaned_data.get('password1'), form.cleaned_data.get("email")
        if "@ms.asay.com.tr" in email:
            
            inactive_user = send_verification_email(self.request, form)
            return render(self.request, "register.html", {"msg":"Hesabınız Başarıyla Oluşturuldu, Mail Adresinize Gönderilen Aktivasyon Linkiyle Lütfen Hesabınızı Doğrulayın."})

        else:
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            
            return render(self.request,"register.html", {"msg":"Hesabınız Başarıyla Oluşturuldu Ama Üyeliğiniz Aktif Değil Lütfen Yöneticiyle İrtibata Geçiniz"})

    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect("/")
        
        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(auth_views.LoginView):
    template_name="login.html"
    
    def form_invalid(self, form):
        user = User.objects.get(username=form.cleaned_data.get("username"))
        if user.check_password(form.cleaned_data.get("password")) and not user.is_active:
            msg = ""
            if "@ms.asay.com.tr" in user.email:
                msg = "Lütfen Hesabınızı E-mail Adresinize Gelen Linkten Aktif Ediniz."
            else:
                msg = "Hesabınız Aktif Değil Lütfen Yöneticiyle İrtibata Geçin"
                
            return render(self.request, "login.html", {"msg":msg})
        
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect("/")
        
        return super().dispatch(request, *args, **kwargs)