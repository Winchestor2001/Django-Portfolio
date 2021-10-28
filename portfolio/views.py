from django.shortcuts import render
from .models import AboutInfoConfig, SkillsInfoConfig, Portfolio, FactsInfoConfig
from django.views.generic import DetailView




def home(request):
    AboutInfoConfig_model = AboutInfoConfig.objects.all()
    SkillsInfoConfig_model = SkillsInfoConfig.objects.all()
    Portfolio_model = Portfolio.objects.all()
    FactsInfoConfig_model = FactsInfoConfig.objects.all()
    return render(request, 'base.html',
                  {
                      'aboutInfo': AboutInfoConfig_model,
                      'skillsInfo': SkillsInfoConfig_model,
                      'portfolio': Portfolio_model,
                      'facts': FactsInfoConfig_model
                  })


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio-details.html'
    context_object_name = 'project_detail'




