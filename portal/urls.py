from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^product/?$', 'portal.views.product'),
	url(r'^product/sedan/?', 'portal.views.product_sedan'),
	url(r'^product/hatchback?', 'portal.views.product_hatchback'),
	url(r'^product/mpv?', 'portal.views.product_mpv'),
	url(r'^product/suv?', 'portal.views.product_suv'),
	url(r'^product/commercial?', 'portal.views.product_commercial'),
	url(r'^product/sport?', 'portal.views.product_sport'),
	url(r'^product/hybrid?', 'portal.views.product_hybrid'),
)