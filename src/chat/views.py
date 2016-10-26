from django.shortcuts import render

from django.views import generic

from . import models


class MessageView(generic.CreateView):
    model = models.Message
    fields = ['username', 'message']

    def get_initial(self):
        initial = self.initial.copy()
        username = self.request.session.get('username', None)
        if username:
            initial['username'] = username
        return initial

    def form_valid(self, form):
        self.object = form.save()
        self.request.session['username'] = self.object.username
        return super(MessageView, self).form_valid(form)

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        return context
