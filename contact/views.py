# from django.shortcuts import render

# # Create your views here.
# def contact(request):
#     return render(request, 'contact/contact.html')

# from django.shortcuts import render, redirect
# from .forms import ContactForm
# from .models import ContactMessage

# def contact(request):
#     if request.method == 'POST':
#         # Si le formulaire est soumis
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Récupérer les données du formulaire
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Sauvegarder les données dans la base de données
#             ContactMessage.objects.create(name=name, email=email, message=message)

#             # Rediriger l'utilisateur vers une page de succès
#             return redirect('contact_success')
#     else:
#         # Si la méthode est GET, afficher un formulaire vide
#         form = ContactForm()

#     # Afficher le formulaire dans le template
#     return render(request, 'contact/contact.html', {'form': form})

##########################################################################################
# from django.shortcuts import render
# from .forms import ContactForm
# from .models import ContactMessage

# def contact(request):
#     success = False  # Indicateur de succès
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Récupérer les données du formulaire
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Sauvegarder les données dans la base de données
#             ContactMessage.objects.create(name=name, email=email, message=message)

#             # Marquer le succès
#             success = True
#     else:
#         form = ContactForm()

#     # Passer l'indicateur de succès au template
#     return render(request, 'contact/contact.html', {'form': form, 'success': success})


# from django.core.mail import send_mail
# from django.shortcuts import render, redirect
# from .forms import ContactForm

# def contact(request):
#     success = False  # Indicateur de succès
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Récupérer les données du formulaire
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Envoyer un email
#             subject = f"Message de {name} via le formulaire de contact"
#             email_message = f"""
#             Nom: {name}
#             Email: {email}
#             Message:
#             {message}
#             """
#             send_mail(
#                 subject,  # Sujet de l'email
#                 email_message,  # Corps de l'email
#                 'fiarmasome@gmail.com',  # Expéditeur (votre adresse)
#                 ['fiarmasome@gmail.com'],  # Destinataire (votre adresse)
#                 fail_silently=False,
#             )

#             # Marquer le succès
#             success = True
#     else:
#         form = ContactForm()

#     # Passer l'indicateur de succès au template
#     return render(request, 'contact/contact.html', {'form': form, 'success': success})


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    success = False  # Indicateur de succès
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Envoyer un email à vous-même
            subject = f"Message de {name} via le formulaire de contact"
            email_message = f"""
            Nom: {name}
            Email: {email}
            Message:
            {message}
            """
            send_mail(
                subject,  # Sujet de l'email
                email_message,  # Corps de l'email
                'fiarmasome@gmail.com',  # Expéditeur (votre adresse)
                ['fiarmasome@gmail.com'],  # Destinataire (votre adresse)
                fail_silently=False,
            )

            # Envoyer une réponse automatique à la personne
            response_subject = "Merci pour votre message"
            response_message = f"""
            Bonjour {name},
            
            Merci de m'avoir contacté. J'ai bien reçu votre message et je vous répondrai dès que possible.
            
            Cordialement,
            Fiarma Landry SOME
            """
            send_mail(
                response_subject,  # Sujet de l'email
                response_message,  # Corps de l'email
                'fiarmasome@gmail.com',  # Expéditeur (votre adresse)
                [email],  # Destinataire (l'adresse de la personne)
                fail_silently=False,
            )

            # Marquer le succès
            success = True
    else:
        form = ContactForm()

    # Passer l'indicateur de succès au template
    return render(request, 'contact/contact.html', {'form': form, 'success': success})