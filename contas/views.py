from django.shortcuts import render
from .models import Pessoa,Login,Conta

def mostrar_formulario_cadastro(request):
  if request.method == 'POST':
    pessoa = Pessoa()
    pessoa.nome = request.POST.get('nome')
    pessoa.cpf = request.POST.get('cpf')
    pessoa.email = request.POST.get('email')
    pessoa.telefone = request.POST.get('telefone')
    pessoa.genero = request.POST.get('genero')
    pessoa.save()
    return render(request, 'conta.html')
  return render(request, 'index.html')

def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()
  return render(request, 'pessoas.html', {'dados': pessoas})

def login(request):
  if request.method == 'POST':
    email_form = request.POST.get('email')
    email_banco = Pessoa.objects.filter(email=email_form).first()
    if email_banco is not None:
      return render(request, 'filtrado.html', {'pessoa': email_banco})
    else:
      return render(request, 'naotem.html',)
  return render(request, 'login.html')

def conta(request):
  if request.method == 'POST':
    conta_form = request.POST.get('email')
    email_banco = Pessoa.objects.filter(email=conta_form).first()
    if email_banco is not None:
      conta = Conta()
      conta.saldo = request.POST.get('saldo')
      conta.agencia = request.POST.get('agencia')
      conta.numero_conta = request.POST.get('numero_conta')
      conta.pessoa = email_banco
      conta.save()
      return render(request,'login.html')
    else:
      return render(request,'conta.html',{'msg': 'Essa conta não existe'})    
  return render(request,'conta.html')    