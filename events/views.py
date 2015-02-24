from models import Events
from braces.views import LoginRequiredMixin

class RushCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = '.'
    form_class = CreateEventForm
    model = Events
    def get_success_url(self):
        return reverse('rushtracker:index')