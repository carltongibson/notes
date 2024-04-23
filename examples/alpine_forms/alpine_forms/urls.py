from django import forms
from django.db import models
from django.shortcuts import render
from django.urls import path


class ComponenentChoices(models.TextChoices):
    ORM = "ORM", "ORM"
    ADMIN = "ADMIN", "Admin"
    STATICFILES = "STATICFILES", "Static Files"


class ExampleForm(forms.Form):
    favourite_framework = forms.CharField(
        label="What's your favourite web framework?",
        template_name="example-form.html#favourite-framework",
        widget=forms.TextInput(
            attrs={
                "x-on:change": "checkValid",
            }
        ),
    )

    favourite_component = forms.ChoiceField(
        label="What's your favourite component?",
        choices=[(None, "---")] + ComponenentChoices.choices,
        widget=forms.Select(
            attrs={
                "x-model": "component",
            }
        ),
    )

    compressor = forms.ChoiceField(
        template_name="example-form.html#compressor",
        label="Do you use django-compressor?",
        choices=[("YES", "Yes"), ("NO", "No")],
        widget=forms.RadioSelect(
            attrs={
                "x-on:change": "checkHero",
            }
        )
    )

    template_name = "example-form.html"


def view(request):
    context = {
        "form": ExampleForm(),
    }
    return render(request, "view-template.html", context=context)


urlpatterns = [
    path("", view),
]
