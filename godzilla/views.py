from django.views.generic import TemplateView


class GodzillaView(TemplateView):
    template_name = 'godzilla/index.html'
