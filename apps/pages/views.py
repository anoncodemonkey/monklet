from django.views.generic import TemplateView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import EnquiryForm


class PagesView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )
        return context


class LandingPageView(PagesView):
    template_name = "landing_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context["redirect_url"] = "/console/"
        return context


def comingsoon(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("enquiry_success"))
    else:
        form = EnquiryForm()

    return render(
        request,
        "comingsoon.html",
        {"form": form, "layout_path": TemplateHelper.set_layout("layout_blank.html")},
    )


def enquiry_success(request):
    return render(request, "enquiry_success.html",
                  {"layout_path": TemplateHelper.set_layout("layout_blank.html")})
