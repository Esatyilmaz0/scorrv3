from django.http.response import JsonResponse
from excel_app.models import HamVeri, Log, RaporGirdiler, RaporReferanslari, SorguList
from django.shortcuts import redirect, render
from .scor3 import rapor_calistir

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url="/register")
def index(request):
    rapor_girdiler = HamVeri.objects.all()
    saha_no_list = []
    for girdi in rapor_girdiler:
        if girdi.saha_no not in saha_no_list:
            saha_no_list.append(girdi.saha_no)
    
    return render(request,"index.html", context={"data":saha_no_list})

@login_required(login_url="/register")
def girdiler(request):
    saha_no = request.GET.get("saha_no")
    ham_veriler = list(HamVeri.objects.filter(saha_no=saha_no).values("saha_no", "saha_kodu", "ekipman_parca_kodu", "parca_tanimi", "quantity"))
    sorgu_list = list(SorguList.objects.all().values("sorgu_no", "kontrol", "ref_grup", "kategori"))
    rapor_referanslari = list(RaporReferanslari.objects.all().values("sorgu_no", "ref", "ekipman_parca_kodu"))
    girdiler = rapor_calistir(ham_veriler, saha_no, sorgu_list, rapor_referanslari)
    log = Log(user=request.user)
    log.description = f"{saha_no} Kodlu Saha No'nun Rapor Girdilerini Oluşturdu."
    log.save()
    return render(request, "girdiler.html", {"data":girdiler})

@login_required(login_url="/register")
def updateAciklama(request):
    girdi_id = request.GET["girdi_id"]
    girdi = RaporGirdiler.objects.get(id=girdi_id)
    girdi.aciklama = request.GET["aciklama"]
    girdi.save()
    log = Log(user=request.user)
    log.description = f"{girdi_id} Id'li Girdinin Açıklamasını Değiştirdi."
    log.save()
    return JsonResponse({"Msg":"Success"})




# Sign Up View
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = 'register.html'
    def form_valid(self, form):
        
        user_form = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return user_form
    
    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)
