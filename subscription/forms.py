#coding: utf-8
from django import forms
from subscription.models import Subscription
from subscription import validators 

#ugettext para trabalhar na hora de criar um form na mão
from django.utils.translation import ugettext as _
EMPTY_VALUES = (None, '')


class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widget = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs))
        super(PhoneWidget, self).__init__(widget, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return [None, None]

class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField()
        )
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in EMPTY_VALUES:
                raise forms.ValidationError(u'DD inválido')
            if data_list[1] in EMPTY_VALUES:
                raise forms.ValidationError(u'Telefone inválido')
            return '%s-%s' % tuple(data_list)
        return None

class SubscriptionForm(forms.ModelForm):
    
    phone = PhoneField(label=_("Telefone"))

    class Meta:
       model = Subscription
       exclude = ('created_at','paid')

    def clean(self):
        super(SubscriptionForm, self).clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise forms.ValidationError(_(u'Você precisa informar seu email ou telefone'))
        return self.cleaned_data
            

#Se fosse criar na mão
#class SubscriptionForm(forms.Form):
#    name = forms.CharField(label=_('Nome'), max_length=100)
#    cpf = forms.CharField(label=_('CPF'), max_length=11, min_length=11, validators=[validators.CpfValidator] )
#    email = forms.EmailField(label=_("E-mail"))
#    phone = forms.CharField(label=_('Telefone'), required=False, max_length=20)

#    def _unique_check(self, fieldname, error_message):
 #       param = { fieldname: self.cleaned_data[fieldname] }
  #      try:
   #         s = Subscription.objects.get(**param)
    #    except Subscription.DoesNotExist:
     #       return self.cleaned_data[fieldname]
      #  raise forms.ValidationError(error_message) 

    #def clean_cpf(self):
     #   return self._unique_check('cpf', _(u'CPF já inscrito'))

    #def clean_email(self):
     #   return self._unique_check('email', _(u'E-mail já inscrito'))


    #def clean(self):
     #   if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
      #      raise forms.ValidationError(_(u'Você precisa informar seu email ou telefone'))
       # return self.cleaned_data
            
        

