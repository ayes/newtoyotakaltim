from django.shortcuts import render_to_response
from django.template import RequestContext

def main(request):
	return render_to_response('portal_main.html',{}, RequestContext(request))

def product(request):
	return render_to_response('portal_product.html',{}, RequestContext(request))

def product_sedan(request):
	return render_to_response('portal_product_sedan.html',{}, RequestContext(request))

def product_sedan_camry(request):
	return render_to_response('portal-product-sedan-camry.html',{}, RequestContext(request))

def product_sedan_all_new_vios(request):
	return render_to_response('portal-product-sedan-all-new-vios.html',{}, RequestContext(request))

def product_sedan_all_new_corolla_altis(request):
	return render_to_response('portal-product-sedan-all-new-corolla-altis.html',{}, RequestContext(request))

def product_hatchback(request):
	return render_to_response('portal_product_hatchback.html',{}, RequestContext(request))

def product_hatchback_yaris(request):
	return render_to_response('portal-product-hatchback-yaris.html',{}, RequestContext(request))

def product_hatchback_agya(request):
	return render_to_response('portal-product-hatchback-agya.html',{}, RequestContext(request))

def product_hatchback_etios_valco(request):
	return render_to_response('portal-product-hatchback-etios-valco.html',{}, RequestContext(request))

def product_mpv(request):
	return render_to_response('portal_product_mpv.html',{}, RequestContext(request))

def product_mpv_alphard(request):
	return render_to_response('portal-product-mpv-alphard.html',{}, RequestContext(request))

def product_mpv_nav1(request):
	return render_to_response('portal-product-mpv-nav1.html',{}, RequestContext(request))

def product_mpv_kijang_innova(request):
	return render_to_response('portal-product-mpv-kijang-innova.html',{}, RequestContext(request))

def product_mpv_avanza_veloz(request):
	return render_to_response('portal-product-mpv-avanza-veloz.html',{}, RequestContext(request))

def product_mpv_avanza(request):
	return render_to_response('portal-product-mpv-avanza.html',{}, RequestContext(request))

def product_suv(request):
	return render_to_response('portal_product_suv.html',{}, RequestContext(request))

def product_suv_land_cruiser(request):
	return render_to_response('portal-product-suv-land-cruiser.html',{}, RequestContext(request))

def product_suv_new_fortuner(request):
	return render_to_response('portal-product-suv-new-fortuner.html',{}, RequestContext(request))

def product_suv_new_rush(request):
	return render_to_response('portal-product-suv-new-rush.html',{}, RequestContext(request))

def product_commercial(request):
	return render_to_response('portal_product_commercial.html',{}, RequestContext(request))

def product_commercial_hiace(request):
	return render_to_response('portal-product-commercial-hiace.html',{}, RequestContext(request))

def product_commercial_dyna(request):
	return render_to_response('portal-product-commercial-dyna.html',{}, RequestContext(request))

def product_commercial_hilux_d_cab(request):
	return render_to_response('portal-product-commercial-hilux-d-cab.html',{}, RequestContext(request))

def product_commercial_hilux_s_cab(request):
	return render_to_response('portal-product-commercial-hilux-s-cab.html',{}, RequestContext(request))

def product_sport(request):
	return render_to_response('portal-product-sport.html',{}, RequestContext(request))

def product_sport_toyota_86(request):
	return render_to_response('portal-product-sport-toyota-86.html',{}, RequestContext(request))

def product_hybrid(request):
	return render_to_response('portal-product-hybrid.html',{}, RequestContext(request))

def product_hybrid_prius(request):
	return render_to_response('portal-product-hybrid-prius.html',{}, RequestContext(request))

def product_hybrid_camry_hybrid(request):
	return render_to_response('portal-product-hybrid-camry-hybrid.html',{}, RequestContext(request))