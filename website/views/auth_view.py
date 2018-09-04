from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

# from website.forms import UserForm, ProductForm, ProfileForm I got this from Bangazon 2.0, but not sure how to use yet.#


# Create your views here.
def register(request):
    """Handles the creation of a new user for authentification.

    Method Arguments:
        request -- The full HTTP request object
    """

    #A boolean value for telling the template wheater the registartion was successful.
    #Set to False initially. Code changes value to True when registration succeeds.
    registered = False


    #Create a new user by invoking the 'create_user' helper method
    #on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        profile_form = ProfileForm()
        template_name = 'register.html'
        return render(request, template_name, {'user_form': user_form, 'profile_form':profile_form})
        #Need to check on forms


# User the login_required() decorate to ensure only those logged in can access the view.
def login_user(request):
    """Handles the creation of a new user for authentification.

    Arguments:
        request -- The full HTTP request object
    """
    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is HTTP POST, try to pull out the relevant information.
    if request.method == "POST":

        #User the built-in authentification method to verify.
        username=request.POST['username']
        password=request.POST['password']
        authenticated_user=authenticate(username=username, password=password)

        # Ifauthentification was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('/')

        else:
            #Can't log user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid loging details supplied.")
    return render(request, 'login.html', {}, context)

@login_required
def user_logout(request):
    #Since we know the user is logged in, we can now just log them out.
    logout(request)

    return HttpResponseRedirect('/')