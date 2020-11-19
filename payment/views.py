import braintree
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
#import weasyprint
from io import BytesIO


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        valid = False
        if order.customer.total_points >= order.get_total_cost():
            valid = True
        if valid:
            order.customer.spend_points(order.get_total_cost())
            order.paid = True
            order.save()
            # send email to customer
            subject = 'MavPoints - Invoice no. {}'.format(order.id)
            message = 'Thank you for shopping at MavPoints. ' \
                      'Your total bill to your rewards account was ' \
                      + str(order.get_total_cost()) + ' points.' \
                      ' Your new account balance is ' + str(order.customer.total_points)
            email = EmailMessage(subject,
                                 message,
                                 'isqa.email.recieve@gmail.com',
                                 [order.email])
            email.send()
            return redirect('payment:done')
        else:
            order.delete()
            return redirect('payment:canceled')
    else:
        return render(request,
                      'payment/process.html',
                      {'order': order})


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')

