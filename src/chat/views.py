from django.shortcuts import render

from django.views import generic

from . import models


from authentication.views import UserIDRequiredMixin
from . import models


class MessageView(UserIDRequiredMixin, generic.CreateView):
    model = models.Message
    fields = ['message']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.username = self.request.user.username
        self.request.session['username'] = self.request.user.username
        return super(MessageView, self).form_valid(form)

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        return context
