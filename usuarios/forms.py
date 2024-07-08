from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(label="Nome de Login", required=True, max_length=100, widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex. João Silva',
            }
        ))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ), label="Senha", required=True, max_length=70)
    

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label="Nome de Login", required=True, max_length=100, widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex. João Silva',
            }
        ))
    email = forms.EmailField(label="E-mail", required=True, max_length=100, widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex. joao@gmail.com',
            }
        ))

    senha1 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ), label="Senha", required=True, max_length=70)
    
    senha2 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        ), label="Confirme a sua senha", required=True, max_length=70)