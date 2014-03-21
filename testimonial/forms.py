from django import forms
from testimonial.models import *

class KomentarForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(KomentarForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Komentar
		fields = ('nama', 'bekerja', 'jabatan', 'email', 'komentar')