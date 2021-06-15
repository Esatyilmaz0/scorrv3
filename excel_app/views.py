from django.contrib import auth
from django.contrib.auth import decorators
from excel_app.forms import CustomUserForm, SignupForm
from django.http.response import JsonResponse
import pandas
from excel_app.models import Log, Rapor, RaporEnvanter, SayimRapor, RaporReferanslari, SayimSonrasiEnvanter, SorguList
from django.shortcuts import redirect, render
from verify_email.email_handler import send_verification_email
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import os
from django.core.mail import EmailMessage
from .Scor_V5_ import rapor_calistir
from django.views.decorators.csrf import csrf_exempt
from .decorators import authUser

def permissionDenied(request):
    return render(request, "permission_denied.html")

@csrf_exempt
def satirEkle(request):
    rapor_id, saha_no, saha_kod, department_code, ekipman_parca_kodu, ekipman_seri_no, parca_tanimi, sayim, aciklama = request.POST.values()
    
    rapor = Rapor.objects.get(id=rapor_id)
    sayim_girdi = SayimSonrasiEnvanter(saha_no=saha_no, saha_kodu=saha_kod, ekipman_seri_no=ekipman_seri_no, ekipman_parca_kodu=ekipman_parca_kodu, parca_tanimi=parca_tanimi, department_code=department_code, quantity=0, aciklama=aciklama, sayim=int(sayim), rapor=rapor)
    sayim_girdi.save()
    
    return render(request, "bakim_envanter_satir_ekle.html", {"satir":sayim_girdi})

def getHamVeriAndCreate(request, child_rapor_id=0):
    my_file = request.FILES["excelFile"]
        
    fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # defaults to   MEDIA_ROOT
    filename = fs.save(my_file.name, my_file)
    
    ham_veri = pandas.read_excel(settings.MEDIA_ROOT +"/" +  filename, engine="openpyxl")
    
    sorgu_list = pandas.read_excel(settings.MEDIA_ROOT +"/" +  "Sorgu_List.xlsx", engine="openpyxl")
    sorgu_ref = pandas.read_excel(settings.MEDIA_ROOT +"/" +  "Sorgu_Ref.xlsx", engine="openpyxl")

    rapor = Rapor(user=request.user)
    if child_rapor_id != 0:
        rapor.child = Rapor.objects.get(id=child_rapor_id)
    
    rapor.save()
    
    girdiler = rapor_calistir(ham_veri, sorgu_list, sorgu_ref, rapor=rapor)

    log = Log(user=request.user, saha_no="", saha_kod="")
    log.description = f"{request.user} Adlı KUllanıcı Yeni Bir Rapor Oluşturdu."
    log.save()
    fs.delete(filename)
    return {"rapor_id": rapor.id, "data": girdiler}

@authUser(permission_user="kontrolcu")
@authUser(permission_user="denetci")
@authUser(permission_user="bakimci")
def home(request):
    if request.user.is_authenticated and not request.user.profile.kontrolcu:
        return redirect("/bakimRapor/")
    elif request.user.is_authenticated and request.user.profile.kontrolcu:
        return redirect("/kontrolRaporlar/")
    return render(request, "login.html")

def clear(request, param):
    if param == "referans":
        RaporReferanslari.objects.all().delete()
        return redirect("https://testscorr.pythonanywhere.com/admin/excel_app/raporreferanslari/")
    elif param == "sorgulist":
        SorguList.objects.all().delete()
        return redirect("https://testscorr.pythonanywhere.com/admin/excel_app/sorgulist/")

"""
Verilen Saha Noya Ait Raporları Getirme View'ı

"""




"""
Rapor Onaylama Kısmı

"""

def raporOnayla(request):
    rapor_id = request.GET.get("rapor_id")
    rapor = Rapor.objects.get(id=rapor_id)
    if rapor.child is not None:
        rapor.child.onay = True
        rapor.child.save()
    rapor.onay = True
    rapor.save()
    
    return JsonResponse({"Msg": "Success"})


"""
İlgili Rapora Ait Girdileri Getirme View'ı
"""


"""
Sayım Sonuç Raporu Oluşturma View'ı

"""
@login_required(login_url="/login")
@csrf_exempt
def sayimSonucRaporuOlustur(request):
    rapor_id = request.POST.get("rapor_id")
    rapor = Rapor.objects.get(id=rapor_id)
    
    rapor.girdiler.all().delete()   
    
    sayim_sonrasi_envanter = rapor.sayim_sonrasi_envanter.all().values("saha_no", "saha_kodu", "ekipman_seri_no", "ekipman_parca_kodu", "parca_tanimi", "department_code", "sayim")
    
    ham_veri = pandas.DataFrame(sayim_sonrasi_envanter)
    sorgu_list = pandas.read_excel(settings.MEDIA_ROOT +"/" +  "Sorgu_List.xlsx", engine="openpyxl")
    sorgu_ref = pandas.read_excel(settings.MEDIA_ROOT +"/" +  "Sorgu_Ref.xlsx", engine="openpyxl")
    
    sayim_sonrasi_envanter = rapor.sayim_sonrasi_envanter.all()
    girdiler = rapor_calistir(ham_veri, sorgu_list, sorgu_ref, rapor=rapor)
    return render(request, "bakım_rapor.html", {"sayim_sonuc_girdiler":girdiler, "bakim_envanter":sayim_sonrasi_envanter, "rapor_id":rapor_id, "rapor":rapor})
    #return redirect("/rapor_getir/?rapor_id=" + rapor_id)



"""
Sayım Rapor Girdisine Ait Açıklama Kısmının Değiştirilmesi View'ı
"""
@login_required(login_url="/login")
def updateAciklama(request):
    girdi_id = request.GET["girdi_id"]
    girdi = SayimRapor.objects.get(id=girdi_id)
    girdi.aciklama = request.GET["aciklama"]
    girdi.save()
    log = Log(user=request.user)

    log.description = f"{request.user} Adlı Kullanıcı {girdi.saha_no} Saha No ve {girdi.saha_kod} Saha Kodlu {girdi_id} Id'sine Sahip Girdinin Açıklamasını {girdi.aciklama} Şeklinde Değiştirdi."
    log.saha_no = girdi.saha_no
    log.saha_kod = girdi.saha_kod
    log.save()

    return JsonResponse({"Msg":"Success"})

@login_required(login_url="/login")
def bakimEnvanterGirdiUpdate(request):
    aciklama = request.GET.get("aciklama")
    sayim = request.GET.get("sayim")
    girdi_id = request.GET.get("girdi_id")
    girdi = SayimSonrasiEnvanter.objects.get(id=girdi_id)
    girdi.aciklama = aciklama
    girdi.sayim = int(sayim)
    girdi.save()
    log = Log(user=request.user)
    log.description = f"{request.user} Adlı Kullanıcı Sayım Sonrası Envanter Raporundaki {girdi.saha_no} Saha No'lu Ve {girdi.id} ID'sine Sahip Girdiyi Güncelledi."
    log.saha_no = girdi.saha_no
    log.saha_kod = girdi.saha_kodu
    return JsonResponse({"Msg": "Success"})


"""
Ham Veri Dosyasıyla Sayım Sonrası Envanter Ve Sayım Rapor Girdilerini Oluşturma View'ı
"""
@login_required(login_url="/login")
@authUser(redirect_url="/permissionDenied", permission_user="bakimci")
def bakimRaporOlustur(request):
    if request.method == "POST" and request.FILES['excelFile']:
        context = getHamVeriAndCreate(request)
        rapor_id = context["rapor_id"]
        rapor = Rapor.objects.get(id=rapor_id)
        sayim_sonrasi_envanter = rapor.sayim_sonrasi_envanter.all()
        return render(request, "bakım_rapor.html", {"bakim_envanter":sayim_sonrasi_envanter, "sayim_sonuc_girdiler":context["data"], "rapor_id":rapor.id, "rapor":rapor})

    return render(request, "bakım_rapor.html")


"""
Sayım Sonrası Envanter Getirme View'ı
"""



@login_required(login_url="/login")
def raporEnvanterUpdate(request):
    girdi_id = request.GET.get("girdi_id")
    girdi = RaporEnvanter.objects.get(id=girdi_id)
    girdi.aciklama = request.GET.get("aciklama")
    girdi.save()
    log = Log(user=request.user)

    log.description = f"{request.user} Adlı Kullanıcı Rapor Envanterindeki {girdi.saha_no} Saha No ve {girdi.user} Saha Kodlu {girdi_id} Id'sine Sahip Girdinin Açıklamasını {girdi.aciklama} Şeklinde Değiştirdi."
    log.saha_no = girdi.saha_no
    log.saha_kod = girdi.user
    log.save()
    return JsonResponse({"Msg":"Success"})

@login_required(login_url="/login")
@authUser(permission_user="kontrolcu")
def kontrolRaporOlustur(request):
    if request.method == "POST" and request.FILES['excelFile']:
        try:
            context = getHamVeriAndCreate(request, child_rapor_id=request.POST.get("child_rapor_id"))
            rapor = Rapor.objects.get(id=context["rapor_id"])
        
            child_rapor_girdiler = rapor.child.girdiler.filter(is_sayim_sonrasi=True)
            context["kontrol_edilecek_girdiler"] = child_rapor_girdiler
            context["kontrol_envanter"] = rapor.rapor_envanter.all()
            context["rapor"] = rapor
            return render(request, "kontrol_rapor.html", context)
        except Exception as e:
            return render(request, "kontrol_rapor.html", {"Error":e})
            
    return render(request, "kontrol_rapor.html")


@csrf_exempt
def sendMailKontrolRapor(request):
    rapor_id = request.POST.get("rapor_id")
    
    mail_body = request.POST.get("mail_body")
    rapor = Rapor.objects.get(id=rapor_id)
    child_rapor = rapor.child
    user_email = child_rapor.user.email
    rapor_girdiler = rapor.girdiler.all().values()
    
    rapor_sayim_sonuc_rapor = rapor_girdiler
    rapor_sayim_sonrasi_envanter = rapor.rapor_envanter.all().values()
    rapor_child_sayim_sonuc_girdiler_df = pandas.DataFrame(rapor.child.girdiler.all().values()).drop(["id", "created_at", "is_sayim_sonrasi"], axis=1)
    
    
    file_name = f"{rapor.child.saha_no}_{rapor.child.saha_kod}_{rapor.child.id}_kontrol.xlsx"
    output_path = os.path.join(settings.BASE_DIR, "media/send_mail/") + file_name
    
    writer = pandas.ExcelWriter(output_path)
    rapor_sayim_sonuc_rapor_df = pandas.DataFrame(rapor_sayim_sonuc_rapor).drop(["id", "created_at", "is_sayim_sonrasi"], axis=1)
    rapor_sayim_sonrasi_envanter_df = pandas.DataFrame(rapor_sayim_sonrasi_envanter).drop(["id"], axis=1)
    

    rapor_child_sayim_sonuc_girdiler_df.to_excel(writer, sheet_name="Bakım Raporu")
    rapor_sayim_sonrasi_envanter_df.to_excel(writer, sheet_name="Kontrol Envanter")
    rapor_sayim_sonuc_rapor_df.to_excel(writer, sheet_name="Kontrol Raporu")
    
    writer.save()
    
    mail_subject = f"{child_rapor.saha_no} - {child_rapor.saha_kod} {child_rapor.id} nolu Kontrol Raporu, {child_rapor.user} "
    if child_rapor.onay == True:
        mail_subject += " Onaylı"
    else:
        mail_subject += " Tekrar Sayılacak"
    email = EmailMessage(subject=mail_subject, body=mail_body, from_email="scor.rapor@gmail.com",
                         to=[user_email])
    email.attach_file(output_path)
    
    email.send()
    os.remove(output_path)
    
    return JsonResponse({"Msg":"Success"})

def raporHatali(request):
    rapor_id = request.GET.get("rapor_id")
    rapor = Rapor.objects.get(id=rapor_id)
    rapor.hatali = True
    rapor.onay = False
    rapor.child.hatali = True
    rapor.child.onay = False
    rapor.child.save()
    rapor.save()
    return JsonResponse({"Msg":"Success"})

@csrf_exempt
def sendMailRapor(request):
    rapor_id = request.POST.get("rapor_id")
    mail_subject = request.POST.get("mail_subject")
    mail_body = request.POST.get("mail_body")
    rapor = Rapor.objects.get(id=rapor_id)
    rapor_girdiler = rapor.girdiler.all().values()
    
    rapor_sayim_sonuc_rapor = rapor_girdiler
    
    rapor_sayim_sonrasi_envanter = rapor.sayim_sonrasi_envanter.all().values()
    
    email_list = [email.replace("\r", "") for email in rapor.department_code.emails.split("\n")]
    
    file_name = f"{rapor.saha_no}_{rapor.saha_kod}_{rapor.id}_bakım.xlsx"
    output_path = os.path.join(settings.BASE_DIR, "media/send_mail/") + file_name
    
    writer = pandas.ExcelWriter(output_path)
    
    rapor_sayim_sonuc_rapor_df = pandas.DataFrame(rapor_sayim_sonuc_rapor).drop(["id", "created_at", "is_sayim_sonrasi"], axis=1)
    rapor_sayim_sonrasi_envanter_df = pandas.DataFrame(rapor_sayim_sonrasi_envanter).drop(["id"], axis=1)

    rapor_sayim_sonrasi_envanter_df.to_excel(writer, sheet_name="Bakım Envanter")
    rapor_sayim_sonuc_rapor_df.to_excel(writer, sheet_name="Bakım Raporu")
    
    writer.save()

    mail_subject = f"{rapor.saha_no} - {rapor.saha_kod} {rapor.id} nolu Bakım Raporu, {rapor.user}"
    email = EmailMessage(subject=mail_subject, body=mail_body, from_email="scor.rapor@gmail.com",
                         to=email_list)
    email.attach_file(output_path)

    email.send()
    
    os.remove(output_path)
        
    return JsonResponse({"msg":"Success"})
    

# Sign Up View

class SignUpView(CreateView):
    form_class = SignupForm
    success_url = "/"
    template_name = 'register.html'

    def form_valid(self, form):
        username, password, email = form.cleaned_data.get('username'), form.cleaned_data.get('password1'), form.cleaned_data.get("email")
        if "@ms.asay.com.tr" in email:

            inactive_user = send_verification_email(self.request, form)
            return render(self.request, "register.html", {"msg": "Hesabınız Başarıyla Oluşturuldu, Mail Adresinize Gönderilen Aktivasyon Linkiyle Lütfen Hesabınızı Doğrulayın."})

        else:
            form.save()
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()

            return render(self.request,"register.html", {"msg": "Hesabınız Başarıyla Oluşturuldu Ama Üyeliğiniz Aktif Değil Lütfen Yöneticiyle İrtibata Geçiniz"})

    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect("/")

        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(auth_views.LoginView):
    template_name = "login.html"
    form_class = CustomUserForm
    
    def form_valid(self, form):
        user = User.objects.get(username=form.cleaned_data.get("username"))
        if user.check_password(form.cleaned_data.get("password")) and not user.is_active:
            msg = ""
            if "@ms.asay.com.tr" in user.email:
                msg = "Lütfen Hesabınızı E-mail Adresinize Gelen Linkten Aktif Ediniz."
            else:
                msg = "Hesabınız Aktif Değil Lütfen Yöneticiyle İrtibata Geçin"

            return render(self.request, "login.html", {"msg": msg})
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated and request.user.profile.bakimci):
            return redirect("/bakimRapor")
        elif (request.user.is_authenticated and request.user.profile.kontrolcu):
            return redirect("/kontrolRaporlar")
        elif (request.user.is_authenticated and request.user.profile.denetci):
            return redirect("/bakimRapor")
        elif (request.user.is_authenticated):
            return render(request, "permission_denied.html")
        
        return super().dispatch(request, *args, **kwargs)