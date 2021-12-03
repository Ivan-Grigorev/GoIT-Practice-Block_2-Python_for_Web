from django_registration.forms import RegistrationForm
from users.models import SportUser


class SportUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = SportUser