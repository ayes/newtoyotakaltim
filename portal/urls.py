from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^product/?$', 'portal.views.product'),

	url(r'^product/sedan/?$', 'portal.views.product_sedan'),
	url(r'^product/sedan/camry/?', 'portal.views.product_sedan_camry'),
	url(r'^product/sedan/all-new-vios/?', 'portal.views.product_sedan_all_new_vios'),
	url(r'^product/sedan/all-new-corolla-altis/?', 'portal.views.product_sedan_all_new_corolla_altis'),

	url(r'^product/hatchback/?$', 'portal.views.product_hatchback'),
	url(r'^product/hatchback/yaris/?', 'portal.views.product_hatchback_yaris'),
	url(r'^product/hatchback/agya/?', 'portal.views.product_hatchback_agya'),
	url(r'^product/hatchback/etios-valco/?', 'portal.views.product_hatchback_etios_valco'),

	url(r'^product/mpv/?$', 'portal.views.product_mpv'),
	url(r'^product/mpv/alphard/?', 'portal.views.product_mpv_alphard'),
	url(r'^product/mpv/nav1/?', 'portal.views.product_mpv_nav1'),
	url(r'^product/mpv/kijang-innova/?', 'portal.views.product_mpv_kijang_innova'),

	url(r'^product/suv/?$', 'portal.views.product_suv'),
	url(r'^product/suv/land-cruiser/?', 'portal.views.product_suv_land_cruiser'),
	url(r'^product/suv/new-fortuner/?', 'portal.views.product_suv_new_fortuner'),
	url(r'^product/suv/new-rush/?', 'portal.views.product_suv_new_rush'),

	url(r'^product/commercial/?$', 'portal.views.product_commercial'),
	url(r'^product/commercial/hiace/?', 'portal.views.product_commercial_hiace'),
	url(r'^product/commercial/dyna/?', 'portal.views.product_commercial_dyna'),
	url(r'^product/commercial/hilux-d-cab/?', 'portal.views.product_commercial_hilux_d_cab'),
	url(r'^product/commercial/hilux-s-cab/?', 'portal.views.product_commercial_hilux_s_cab'),

	url(r'^product/sport/?$', 'portal.views.product_sport'),
	url(r'^product/sport/toyota-86/?', 'portal.views.product_sport_toyota_86'),

	url(r'^product/hybrid/?$', 'portal.views.product_hybrid'),
	url(r'^product/hybrid/prius/?', 'portal.views.product_hybrid_prius'),
	url(r'^product/hybrid/camry-hybrid/?', 'portal.views.product_hybrid_camry_hybrid'),
)