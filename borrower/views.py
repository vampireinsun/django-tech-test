from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import HttpResponse, HttpResponseRedirect, render_to_response, Http404
from django.http import HttpResponseBadRequest
from borrower.forms import UserForm, BorrowerForm, BorrowerBusinessForm
from django.template.context_processors import csrf
from borrower.models import BorrowerBusinesses, Borrower


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        borrower_form = BorrowerForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and borrower_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            borrower, created = Borrower.objects.get_or_create(
                    user_id=user.id,
                    telephone_number=borrower_form.cleaned_data["telephone_number"])

            registered = True
        else:
            print user_form.errors, borrower_form.errors
    else:
        user_form = UserForm()
        borrower_form = BorrowerForm()

    return render_to_response(
            'register.html',
            {'user_form': user_form, 'borrower_form': borrower_form, 'registered': registered},
            context)


def login_view(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)


def logout_view(request):
    logout(request)
    context = RequestContext(request)
    return render_to_response('login.html', {}, context)


@login_required
def borrower_profile_view(request):
    context = {}
    context.update(csrf(request))
    if request.method == 'POST':
        borrower_form = BorrowerForm(request.POST)
        if borrower_form.is_valid():
            telephone_number = borrower_form.cleaned_data['telephone_number']
            borrower = Borrower.objects.get(user__id=request.user.id)
            if borrower is not None:
                borrower.telephone_number = telephone_number
                borrower.save()

                return HttpResponseRedirect("/index/")
            else:
                context["errors"] = "Failed to update the borrower's information"
    else:
        try:
            borrower = Borrower.objects.get(user__id=request.user.id)
            borrower_form = BorrowerForm(initial={'telephone_number': borrower.telephone_number})
        except Borrower.DoesNotExist:
            borrower_form = BorrowerForm()

    context['borrower_form'] = borrower_form
    return render_to_response('profile.html', context, context_instance=RequestContext(request))


@login_required
def borrower_update_business_view(request, borrower_business_id):
    context = {}
    context.update(csrf(request))
    borrower = Borrower.objects.get(user__id=request.user.id)

    if request.method == 'POST':
        if borrower_business_id == "0":
            borrower_business_form = BorrowerBusinessForm(request.POST)
        else:
            borrower_business_form = BorrowerBusinessForm(request.POST,
                                                          instance=BorrowerBusinesses.objects.get(
                                                                  id=str(borrower_business_id)))
        if borrower_business_form.is_valid():
            borrower_business = borrower_business_form.save()
            if borrower_business is not None:
                return HttpResponseRedirect("/index/")
            else:
                context["errors"] = "Failed to create/update the business information."
        else:
            context["errors"] = borrower_business_form.errors.__str__()
    else:
        if borrower_business_id == "0":
            borrower_business_form = BorrowerBusinessForm(initial={'borrower': borrower.id})
        else:
            borrower_business_form = BorrowerBusinessForm(
                    instance=BorrowerBusinesses.objects.get(id=borrower_business_id))

    context['borrower_business_form'] = borrower_business_form
    return render_to_response('borrower_business.html', context, context_instance=RequestContext(request))


@login_required
def borrower_business_view(request, borrower_business_id):
    import logging
    logging.getLogger(__name__).error("ddddd==")
    if request.method == "DELETE":
        borrower_business = BorrowerBusinesses.objects.get(id=borrower_business_id)
        if borrower_business is not None:
            borrower_business.delete()
            return HttpResponse("OK")
        else:
            return Http404()
    else:
        return HttpResponseBadRequest("This operation is not allowed.")

