from django.views.generic import TemplateView
import os

class Register(TemplateView):
    template_name = 'register.html'
    def get(self,request,format=None):
        print()
        return super(Register,self).get(request)
    
    """ def get_context_data(self,**kwargs):
        context = super(Register,self).get_context_data(**kwargs)
        return context """