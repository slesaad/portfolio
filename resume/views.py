from django.views.generic import TemplateView

from .models import Education, Experience, Skill, Interest


class ResumeView(TemplateView):
    template_name = "resume/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['educations'] = Education.objects.all()
        context['experiences'] = Experience.objects.all()
        context['skills'] = Skill.objects.all()
        context['interests'] = Interest.objects.all()

        return context
