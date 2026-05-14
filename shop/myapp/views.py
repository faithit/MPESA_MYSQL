from django.shortcuts import render,redirect
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .forms import ProductForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def add_product(request):
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ProductForm()
    return render(request,'addproduct.html',{'form':form})

def home(request):
    return render(request,'pay.html')
def lipa_na_mpesa_online(request):
    if request.method == 'POST':
       phone_number= request.POST[("phone")]
       amount=int(request.POST[("amount")])
       account_reference="firefox"
       transaction_desc="payment of school fees"
       callback_url="https://71d7-41-203-217-161.ngrok-free.app/callback"
       cl=MpesaClient()
       response=cl.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)

       return HttpResponse("payment successful",response)

    return HttpResponse("Invalid request")

@csrf_exempt
def callback(request):
    if request.method == 'POST':
       data=request.POST
       print("callback data",data)
       return JsonResponse({"status":"success"})
    return JsonResponse({"status":"Invalid request"})
def payment_info(request):
    return render(request,'paymentinfo.html')

