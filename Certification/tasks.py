import logging
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail, send_mass_mail
from django.utils.html import strip_tags
from .models import CertifiedCompany

logger = logging.getLogger(__name__)
DEFAULT_FROM_EMAIL = 'aktanarynov566@gmail.com'

@shared_task
def check_certificates():
    today = timezone.now().date()
    notification_periods = [10, 7, 1, 0]

    for period in notification_periods:
        expiration_date = today + timedelta(days=period)
        companies = CertifiedCompany.objects.filter(expiration_date__date=expiration_date)
        logger.info(f'Найдено {companies.count()} компаний с истекающими сертификатами через {period} дней.')

        if companies.exists():
            for company in companies:
                try:
                    send_notification(company, period)
                    logger.info(f'Уведомление отправлено для {company.company_name} ({company.company_email})')
                except Exception as e:
                    logger.error(f'Ошибка при отправке уведомления для {company.company_name}: {str(e)}')


def send_notification(company, days_left):
    subject = f'Уведомление об истечении срока сертификата {company.certificate_name}'
    html_message = generate_html_message(company, days_left)
    plain_message = strip_tags(html_message)

    try:
        send_mail(
            subject, 
            plain_message, 
            DEFAULT_FROM_EMAIL, 
            [company.company_email], 
            fail_silently=False, 
            html_message=html_message
        )
    except Exception as e:
        logger.error(f'Ошибка отправки email: {str(e)}')


def generate_html_message(company, days_left):
    """
    Генерируем HTML-сообщение для отправки уведомлений.
    """
    return f'''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Сертификат Халал</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }}
            .container {{
                width: 100%;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                border: 1px solid #E6E6E6;
            }}
            h1 {{
                color: #333;
                font-size: 22px;
                margin-bottom: 15px;
                line-height: 1.4;
            }}
            p {{
                color: #555;
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 15px;
            }}
            h2 {{
                font-size: 18px;
                margin-top: 20px;
                margin-bottom: 10px;
                color: #333;
            }}
            ul {{
                list-style: none;
                padding-left: 0;
            }}
            li {{
                font-size: 16px;
                margin-bottom: 10px;
            }}
            .phone {{
                font-size: 18px;
                font-weight: bold;
                color: #333;
                margin-top: 10px;
            }}
            .image-container {{
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }}
            .image-container img {{
                width: 100px;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Ваш сертификат {company.certificate_name} истекает через {days_left} дней</h1>
            <p>Уважаемая {company.company_name},</p>
            <p>
                Напоминаем вам, что срок действия вашего сертификата "{company.certificate_name}" истекает через {days_left} дней ({company.expiration_date.strftime('%d.%m.%Y')}).
                Чтобы сохранить статус сертификации и продолжать использовать наши услуги, рекомендуем вам обновить сертификат как можно скорее.
            </p>
            <h2>Что вам нужно сделать:</h2>
            <ul>
                <li>Перейдите в свой личный кабинет на сайте Tez Kabar</li>
                <li>Ознакомьтесь с условиями продления сертификата.</li>
                <li>Подайте заявку на продление в несколько простых шагов</li>
            </ul>
            <p>Если вам требуется помощь или у вас возникли вопросы, свяжитесь с нашей службой:</p>
            <p class="phone">+996 (550) 042 433</p>
            <p class="phone">+996 (550) 042 433</p>

            <div class="image-container">
                <img src="https://via.placeholder.com/100" alt="Phone Icon">
            </div>
        </div>
    </body>
    </html>
    '''
