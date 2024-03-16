from django.shortcuts import render
import razorpay
from .models import Payment
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def view(request):
    return render(request, 'home.html')

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = int(request.POST.get('amount'))*100
        client = razorpay.Client(auth=("rzp_test_SdXIlYfGfq7kia", "CdQbJpWxbHZSTB1Ngt6I1nmx"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        pay = Payment(name=name, email=email, amount=amount, payment_id=payment['id'])
        pay.save()
    else:
        payment = None
        name = None
        email = None
    return render(request, 'index.html', {'payment': payment, "name": name, "email": email})
@csrf_exempt
def success(request):
    if request.method == 'POST':
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Payment.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()

    return render(request, 'success.html')