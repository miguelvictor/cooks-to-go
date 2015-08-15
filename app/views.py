from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'app/index.html'


class WebView(TemplateView):
    template_name = 'app/webindex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WebView, self).get_context_data(**kwargs)
        try:
            active = self.kwargs['page'].lower()
            if active == 'recipe':
                self.template_name = 'web/recipeview.html'
            elif active == 'ingredients':
                self.template_name = 'web/ingredientsView.html'
            elif active == 'virtual-basket':
                self.template_name = 'web/virtualbasket.html'
            elif active == 'settings':
                self.template_name = 'web/settings.html'
        except Exception:
            pass
        return context
