from django.views.generic import TemplateView

from .models import Project


class ProjectsView(TemplateView):
    template_name = "projects/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['projects'] = Project.objects.all()

        return context
