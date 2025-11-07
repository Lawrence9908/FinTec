from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import  gettext_lazy as _

from .emails import send_account_locked_email
from .managers import UserManager

class User(AbstractUser):
    class SecurityQuestion(models.TextChoices):
        MAIDEN_NAME = (
            "maiden_name", _("WHat is your mother's maiden name?")
        )
        FAVORITE_COLOR = (
            "favirite_color",_("What is your favourate color?")
        )
        BIRTH_CITY = (
            "birth_city",_("What is the city where you where born?")
        )
        CHILDHOOD_FRIEND = (
            "chaildhood_friend",_("What is the name of your childhood best friend?")
        )
        
    class AccountStatus(models.TextChoices):
        ACTIVE = "active", _("Active")
        LOCKED = "locked", _("Locked")

    class RoleChoices(models.TextChoices):
        CUSTOMER = "customer", _("CUstomer")
        ACCOUNT_EXECUTIVE = "account_executive", _("Account Executive")
        TELLER = "teller", _("Teller")
        BRANCH_MANAGER = "branch_manager", _("Branch Manager")
    
    security_answer = models.CharField(_("Security Answer"), max_length=30)
    emai = models.EmailField(_("Email"), unique=True, db_index=True)
    first_name  = models.CharField(_("First Name"), max_length=30)
    middle_name  =  models.CharField(_("Middle Name"), max_length=30, blank=True, null=True)
    failed_login_attempts  = models.PositiveSmallIntegerField(default=0)
    last_failed_login  = models.DateTimeField(null=True, blank=True)
    otp = models.CharField(_("OTP"), null=True, blank=True)
    opt_expiry_time = models.CharField(_("OTP Expiry Time"),  null=True, blank=True)

    objects  = UserManager()

    