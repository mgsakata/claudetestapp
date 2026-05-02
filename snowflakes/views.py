from django.views.generic import TemplateView


class SnowflakesView(TemplateView):
    template_name = 'snowflakes/index.html'
