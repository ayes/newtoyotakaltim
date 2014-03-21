from django.contrib import admin
from testimonial.models import *

class KomentarAdmin(admin.ModelAdmin):
	pass

admin.site.register(Komentar, KomentarAdmin)
