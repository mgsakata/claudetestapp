import json
from functools import lru_cache
from pathlib import Path

from django.views.generic import TemplateView

VETTED_PATH = Path(__file__).resolve().parent / 'vetted_dogs.json'


@lru_cache(maxsize=1)
def vetted_titles():
    """Commons file titles that have passed manual content review.

    The slideshow draws only from this list. It is deliberately a pinned
    snapshot rather than a live category query: 'Quality images of dogs' is a
    *technical* rating, so the category itself contains dead, injured and
    otherwise unsuitable animals, and anyone may add more at any time.
    """
    with VETTED_PATH.open(encoding='utf-8') as fh:
        return json.load(fh)


class DogsView(TemplateView):
    template_name = 'dogs/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vetted_titles'] = vetted_titles()
        return context
