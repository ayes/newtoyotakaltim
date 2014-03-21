from django.conf.urls import patterns, include, url
#from portal import views

urlpatterns = patterns('',
	url(r'^testimonial/?', 'testimonial.views.testimonial'),
)