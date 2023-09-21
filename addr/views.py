from django.http import HttpResponse
from django.template import loader
from .forms import AddrForm


def index(request):
    form = AddrForm
    context = {'form': form}
    template = loader.get_template('address/addr.html')
    return HttpResponse(template.render(context, request))
