from django import forms
from .models import Employee;

class EmployeeForm(forms.ModelForm):

     class Meta:
          model = Employee
          fields = ('fullname', 'emp_code', 'mobile', 'position')
          labels = {
               'fullname':'Nome completo',
               'emp_code':'Código do funcionário',
               'mobile':'Telefone ou Celular',
               'position':'Cargo'
          }

     def __init__(self, *args, **kwargs):
          super(EmployeeForm, self).__init__(*args, **kwargs)
          self.fields['position'].empty_label = "Select"
          self.fields['emp_code'].required = False