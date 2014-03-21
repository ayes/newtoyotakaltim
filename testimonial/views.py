from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from testimonial.forms import *
from testimonial.models import *

def get_testi_page(request):
	try:
		return Komentar.objects.filter(aktif=True)
	except:
		return {}

def testimonial(request, berhasil = None):
	if request.method == 'GET':
		form = KomentarForm()
		return render_to_response('portal-testimonial.html', {'form': form, 'berhasil':berhasil, 'testi_list':get_testi_page(request)}, RequestContext(request))
	else:
		form = KomentarForm(request.POST)
		if form.is_valid():
			form.save()
			berhasil = 'Terima Kasih atas Testi anda, testimonial anda akan kami tayangkan setelah disetujui oleh admin'
			return render_to_response('portal-testimonial.html', {'form': form, 'berhasil':berhasil, 'testi_list':get_testi_page(request)}, RequestContext(request))
		else:
			return render_to_response('portal-testimonial.html', {'form': form, 'berhasil':berhasil, 'testi_list':get_testi_page(request)}, RequestContext(request))