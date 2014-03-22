# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
import random
from PIL import Image, ImageFont, ImageDraw
import StringIO
from bsmapp.settings import my_make_path, EMAIL_FROM, EMAIL_TO
from base64 import b64encode
from django.core.mail import send_mail

def generate_code():
	result = ''
	for i in range(0, 4):
		result += random.choice('0123456789')
	
	return result

def make_captcha(request):
	request.session['code'] = generate_code()
	image = Image.new('RGBA', (90, 33), (0, 0, 0, 0))
	draw = ImageDraw.Draw(image)
	draw.text((10, 5), request.session['code'], fill = (0x00, 0x00, 0x00), font = ImageFont.truetype(my_make_path('contact/misc/akbar.ttf'), 23))
	output = StringIO.StringIO()
	image.save(output, format = "PNG")
	contents = output.getvalue()
	output.close()
	return '<img class="capcha" src="data:image/png;base64,' + b64encode(contents) + '" />'

def contacts_page(request, error = None, berhasil = None, success = False):

	if not success:
		nama = request.POST.get('nama', '')
		email = request.POST.get('email', '')
		komentar = request.POST.get('komentar', '')
	
	return render_to_response('contact-contact.html',
		{
		'success': success,
		'captcha': make_captcha(request),
		'error': error,
		'berhasil': berhasil,
		'nama': nama,
		'email': email,
		'komentar': komentar
		}, RequestContext(request))

def feedback_page(request):
	if request.method == 'POST':
		code = request.POST.get('code', '')
		nama = request.POST.get('nama', '')
		email = request.POST.get('email', '')
		komentar = request.POST.get('komentar', '')
		
		if (len(komentar) == 0) or (len(nama) == 0) or (len(email) == 0):
			return contacts_page(request, u'Anda harus mengisi semua bidang')
		
		original_code = request.session.get('code', '')
		
		if code != '' and code == original_code:
			text = u"Pesan baru dari situs.\nPengirim: %s\nE-mail pengirim: %s\npesan: %s" % (nama, email, komentar)
			send_mail(u'Pesan dari situs', text, EMAIL_FROM, [EMAIL_TO], fail_silently = False)
		else:
			return contacts_page(request, u'Salah memasukan kode')

		return contacts_page(request, None, u'Pesan berhasil terkirim!')
	else:
		return HttpResponseRedirect('/contact')
