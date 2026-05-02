from django.views.generic import TemplateView


class DogsView(TemplateView):
    template_name = 'dogs/index.html'
