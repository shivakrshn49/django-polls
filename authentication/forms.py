from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	"""
	Form for registering a new user account.
    
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

	"""
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = { 'class': 'required' }

class RegistrationForm(forms.Form):
	username = forms.RegexField(regex=r'^\w+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_(u'username'))
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,maxlength=75)),
		                        label=_(u'email address'))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_(u'password'))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_(u'password (again)'))

	def clean_username(self):
		"""
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
		try:
			user = User.objects.get(username__iexact=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError(_(u'This username is already taken. Please choose another.'))

	def clean_password2(self)	:
		"""
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_(u'You must type the same password each time'))
		return self.cleaned_data		
			

