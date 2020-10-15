from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from accounts.forms import AccountAuthenticationForm, RegistrationForm
from django.contrib import messages

def home(request):
    context = {}
    return render(request, 'accounts/home.html',context)


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			accounts = authenticate(email=email, password=raw_password)
			login(request, accounts)
			return redirect('login')
		else:
			context['registration_form'] = form
	else: #GET request
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'accounts/register.html', context)

def login_view(request):

	 context = {}

	 user = request.user
	 if user.is_authenticated:
	 	return redirect("home")

	 if request.POST:
	 	form = AccountAuthenticationForm(request.POST)
	 	if form.is_valid():
	 		email = request.POST['email']
	 		password = request.POST['password']
	 		user = authenticate(email=email, password=password)

	 		if user:
	 			login(request, user)
	 			return redirect("home")

	 else:
	 	form = AccountAuthenticationForm()

	 context['login_form'] = form
	 return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
	    
    return render(request,'accounts/logout.html')
       
      


#def logout_view(request):
    #if request.method == 'POST':
        #logout(request)
        #return redirect('logout')
    #return render(request,'accounts/logout.html')


