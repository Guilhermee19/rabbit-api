from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact_view(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        message = req.POST.get('message')

        if email and message:
            try:
                send_mail(
                    'Novo Contato recebido!',
                    f'Nome: \n {name} \n\n Email: \n{email} \n\n Mensagem: \n{message} \n\n',
                    'eu@iamgui.dev',  # O e-mail configurado no Zoho
                    ['eu@iamgui.dev'],  # O destinatário (seu próprio e-mail)
                    fail_silently=False,
                )
                return HttpResponse('E-mail enviado com sucesso!')
            except Exception as e:
                return HttpResponse(f'Erro ao enviar e-mail: {e}', status=500)
        else:
            return HttpResponse('Email ou mensagem não foram fornecidos.', status=400)

    return HttpResponse('Método não permitido', status=405)