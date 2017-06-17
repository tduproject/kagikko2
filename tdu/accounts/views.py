from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.template.loader import get_template
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
from profiles.models import UserProfile

from .forms import (
    RegisterForm,
    LoginForm,
    ChangePasswordForm,
    ForgetPasswordForm,
    PasswordConfirmForm,

)

#ユーザー登録


class CreateUserView(generic.FormView):
    template_name = 'accounts/create.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:create_done')

    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_active = False
        user.email = user.username
        user.save()
        current_site = get_current_site(self.request)
        domain = current_site.domain
 #       subject_template = get_template('mailtemplate/subject.txt')
        message_template = get_template('mailtemplate/message.txt')

        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
            'user': user,
        }


        #subject = subject_template.render(context)
        message = message_template.render(context)
        from_email = settings.EMAIL_HOST_USER
        to = [user.username]

        send_mail('ご登録ありがとうございます',
                 message,
                from_email,
                to
                  )

        return super(CreateUserView, self).form_valid(form)


class CreateDoneView(generic.TemplateView):
    template_name = "accounts/create_done.html"






class CreateCompleteView(generic.TemplateView):
    template_name = 'accounts/create_complete.html'

    def get(self, request, **kwargs):
        token = kwargs.get("token")
        uidb64 = kwargs.get("uidb64")
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and not user.is_active and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            createprofile = UserProfile()
            createprofile.name = user.first_name
            createprofile.email = user.email
            createprofile.save()


            return super(CreateCompleteView, self).get(request, **kwargs)
        else:
            raise Http404



def password_reset(request):
    context = {
        'post_reset_redirect': reverse_lazy('accounts:password_reset_done'),
        'template_name': 'accounts/password_reset_form.html',
        'email_template_name': 'mailtemplate/password_reset/message.txt',
        'subject_template_name': 'mailtemplate/password_reset/subject.txt',
        'password_reset_form': ForgetPasswordForm,
    }
    return auth_views.password_reset(request, **context)


def password_reset_done(request):
    context = {
        'template_name': 'accounts/password_reset_done.html',
    }
    return auth_views.password_reset_done(request, **context)


def password_reset_confirm(request, uidb64, token):
    context = {
        'uidb64': uidb64,
        'token': token,
        'post_reset_redirect': reverse_lazy('accounts:password_reset_complete'),
        'template_name': 'accounts/password_reset_confirm.html',
        'set_password_form': PasswordConfirmForm,
    }
    return auth_views.password_reset_confirm(request, **context)


def password_reset_complete(request):
    context = {
        'template_name': 'accounts/password_reset_complete.html',
    }
    return auth_views.password_reset_complete(request, **context)




def login(request):
    context = {
        'template_name': 'accounts/login.html',
        'authentication_form': LoginForm
    }
    return auth_views.login(request, **context)


def logout(request):
    context = {
        'template_name': 'accounts/login.html'
    }

    return auth_views.logout(request, **context)
