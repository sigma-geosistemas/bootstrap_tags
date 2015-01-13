# coding: utf-8
from django.conf import settings
from django import template
from django.forms import (TimeField,
                          DateField,
                          IntegerField,
                          CharField,
                          DateTimeField,
                          ModelChoiceField,
                          ChoiceField,
                          FloatField,
                          BooleanField,
                          BaseForm)
from django.forms.forms import BoundField

register = template.Library()

BOOTSTRAP_TEMPLATE_SWITCH = {DateField: "bootstrap_tags/date_field.html",
                        DateTimeField: "bootstrap_tags/date_field.html",
                        TimeField: "bootstrap_tags/time_field.html",
                        FloatField: "bootstrap_tags/float_field.html",
                        IntegerField: "bootstrap_tags/int_field.html",
                        CharField: "bootstrap_tags/char_field.html",
                        ModelChoiceField: "bootstrap_tags/list_field.html",
                        ChoiceField: "bootstrap_tags/list_field.html",
                        BooleanField: "bootstrap_tags/boolean_field.html"}

if settings.hasattr("BOOTSTRAP_TEMPLATE_SWITCH"):
    BOOTSTRAP_TEMPLATE_SWITCH.update(settings.BOOTSTRAP_TEMPLATE_SWITCH)


def boots_form(obj):
    """
    the required param, is only used when obj = Field for optional required fields.
    """

    if isinstance(obj, BaseForm):
        return form(obj)

    elif isinstance(obj, BoundField):
        return boots_field(obj)

    else:
        raise Exception, 'Bootstrap template tag recieved a non form or field object'


def boots_field(field):

    """Renderiza um campo com os widgets especificados"""

    field.field.widget.attrs['placeholder'] = field.label

    if type(field.field) in BOOTSTRAP_TEMPLATE_SWITCH:
        t = template.loader.get_template(BOOTSTRAP_TEMPLATE_SWITCH[type(field.field)])
    else:
        t = template.loader.get_template("bootstrap_tags/form_field.html")

    return t.render(template.Context({"field": field}))


def form(form):
    """Renderiza um formulário com os widgets especificados pelo bootstraps-son"""

    form_html = ""

    for fld in form.visible_fields():

        row = boots_field(fld)
        form_html += row

    for fld in form.hidden_fields:

        row = unicode(fld)
        form_html += u"<div style='display:none;'>{0}</div>".format(row)

    return form_html


register.filter("boots_field", boots_field)
register.filter("boots_form", boots_form)
