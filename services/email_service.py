from dataclasses import dataclass, asdict
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.translation import gettext_lazy as _

from users.models import User


@dataclass
class EmailContextBase:
    """Base representation of email context."""
    domain: str
    user: User


@dataclass
class ActivationEmailContext(EmailContextBase):
    """Representation of activation email context."""
    token: str
    encoded_user_id: str
    subject: str = _('Account activation.')


class EmailService:
    """Service is responsible for email operations."""

    _email_templates_path = 'users/emails/'

    def __init__(self, request):
        self.request = request
        self._current_site = get_current_site(self.request)

    def _send_email(self, recipient, template_name, context):
        """
        Prepare and send email message.
        :param recipient: user that should receive email
        :param template_name: name of the template that will be rendered
        :param context: context with which template will be rendered
        """
        html_content = render_to_string(
            f'{self._email_templates_path}/{template_name}',
            context
        )
        msg = EmailMessage(
            subject=context['subject'],
            body=html_content,
            to=[recipient.email]
        )
        msg.send()

    def send_activation_email(self, user, token):
        """
        Send email to activate user profile.
        :param user: user, account of which should be activated
        :param token: activation token
        """
        context = ActivationEmailContext(
            domain=self._current_site.domain,
            user=user,
            token=token,
            encoded_user_id=urlsafe_base64_encode(force_bytes(user.pk))
        )

        self._send_email(user, 'account_activation_email.html', asdict(context))
