from django.views.generic import TemplateView


class BiosphereView(TemplateView):
    template_name = 'biosphere/index.html'
