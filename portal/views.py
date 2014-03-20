from django.shortcuts import render_to_response
from django.template import RequestContext

def main(request):
	return render_to_response('portal_main.html',{}, RequestContext(request))

def product(request):
	return render_to_response('portal_product.html',{}, RequestContext(request))

def product_sedan(request):
	return render_to_response('portal_product_sedan.html',{}, RequestContext(request))

def product_hatchback(request):
	return render_to_response('portal_product_hatchback.html',{}, RequestContext(request))

def product_mpv(request):
	return render_to_response('portal_product_mpv.html',{}, RequestContext(request))

def product_suv(request):
	return render_to_response('portal_product_suv.html',{}, RequestContext(request))

def product_commercial(request):
	return render_to_response('portal_product_commercial.html',{}, RequestContext(request))

def product_sport(request):
	return render_to_response('portal_product_sport.html',{}, RequestContext(request))

def product_hybrid(request):
	return render_to_response('portal_product_hybrid.html',{}, RequestContext(request))