from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from .models import CertifiedCompany


@shared_task
def check_certificates():
    today = timezone.now().date()
    notification_periods = [10, 7, 1, 0]
    for period in notification_periods:
        expiration_date = today + timedelta(days=period)
        companies = CertifiedCompany.objects.filter(expiration_date=expiration_date)
        for company in companies:
            send_notification(company, period)

def send_notification(company, days_left):
    subject = f'Уведомление об истечении срока сертификата {company.certificate_name}'
    message = f'Уважаемая {company.company_name},\n\n' \
              f'Ваш сертификат "{company.certificate_name}" истекает через {days_left} дней ({company.expiration_date}).\n\n' \
              f'Пожалуйста, обновите его вовремя.'    
    send_mail(subject, message, 'aktanarynov566@gmail.com', [company.company_email], fail_silently=False)
