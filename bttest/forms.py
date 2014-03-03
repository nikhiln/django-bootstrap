# -*- coding: utf-8 -*-
from django import forms
 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
 
 
class MemberForm(forms.Form):
    STATUS_TYPES = (
        ('-1','Select'),
        ('Employee','Employee'),
        ('Administrator','Administrator'),
    )
    
    first_name = forms.CharField(
        required = True,
        label = 'First Name'
    )
    last_name = forms.CharField(
        required = True,
        label = 'Last Name'
    )
    email = forms.CharField(
        required = True,
        label = 'Email Address'
    )
    status = forms.ChoiceField(
        choices = STATUS_TYPES,
        required = False,
        label = 'Member Status'
    )
    action = forms.CharField(
        required = False,
        widget = forms.HiddenInput()
    )
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.help_text_inline = True
        self.helper.form_class = 'form-inline main-form'
        add_btn = Submit('btnsubmit', 'Add +', css_class='btn btn-primary offset4')
        self.helper.layout = Layout(
            Div(Field('first_name'), css_class="col-first-name"),
            Div(Field('last_name'), css_class="col-last-name"),
            Div(Field('email'), css_class="col-email"),
            Div(Field('status'), css_class="col-status"),
            Div(Field('action')),
            Div(Div(
                    HTML('<label>&nbsp;</label>'),
                    add_btn, css_class="form-group"
                ), 
                css_class="col-button")
        )
        super(MemberForm, self).__init__(*args, **kwargs)
        
        self.fields['status'].widget.attrs['readonly'] = True