from django import forms
from users.models import Student, Branch

class StudenForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'birthdate', 'branch', 'college')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs):
        self.fields['branch'].queryset = Branch.objects.none()
        
        if 'College' in self.data:
            try:
                college_id = int(self.data.get('college'))
                self.fields['branch'].queryset = Branch.objects.filter(college_id = college_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.isinstance.pk:
            self.fields['branch'].queryset =self.instance.college.branch_set.order_by('name')    




