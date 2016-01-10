from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import HttpResponseRedirect, render_to_response, HttpResponse, Http404
from django.http import HttpResponseBadRequest
from loan.forms import LoanForm
from django.template.context_processors import csrf
from borrower.models import Borrower
from loan.models import Loan, RepaymentHistory
from datetime import datetime


@login_required
def update_loan_view(request, borrower_loan_id):
    context = {}
    context.update(csrf(request))
    if request.method == 'POST':
        if borrower_loan_id == "0":
            loan_form = LoanForm(request.POST)
        else:
            loan_form = LoanForm(request.POST, instance=Loan.objects.get(id=borrower_loan_id))
        if loan_form.is_valid():
            loan = loan_form.save()
            if loan is not None:
                return HttpResponseRedirect("/index/")
            else:
                context["errors"] = "Failed to create/update the loan information."
    else:
        if borrower_loan_id == "0":
            current_date = datetime.now()
            current_date_str = current_date.strftime("%Y-%m-%d")
            loan_form = LoanForm(initial={'borrower': request.user.id, 'applied_date': current_date_str})
        else:
            loan_form = LoanForm(instance=Loan.objects.get(id=borrower_loan_id))

    context['loan_form'] = loan_form
    return render_to_response('loan.html', context, context_instance=RequestContext(request))


@login_required
def loan_view(request, borrower_loan_id):
    if request.method == "DELETE":
        repayment_history_items = RepaymentHistory.objects.filter(loan__id=borrower_loan_id)
        for item in repayment_history_items:
            item.delete()
        borrower_loan = Loan.objects.get(id=borrower_loan_id)
        if borrower_loan is not None:
            borrower_loan.delete()

            return HttpResponse("OK")
        else:
            return Http404()
    else:
        return HttpResponseBadRequest("This operation is not supported.")
