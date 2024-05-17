from models import user
from django.forms import ModelForm, TextInput

class regestration(ModelForm):
    class Meta:
        model = user
        fields = ['name','password']

        widgets = {
            'name': TextInput(attrs={
                #Сюда атрибуты из фронта вставлять чтобы во фронте норм выглядело(для имени)
            }),
            'password':TextInput(attrs={
                #Сюда для пороля
            })
        }