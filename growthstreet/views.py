from django.views.decorators.cache import never_cache
from borrower.models import Borrower, BorrowerBusinesses
from loan.models import Loan
from django.shortcuts import HttpResponse, HttpResponseRedirect, render_to_response


@never_cache
def index_page(request):
    if (request.user.id is not None) and request.user.is_authenticated:
        try:
            borrower = Borrower.objects.get(user__id=request.user.id)
            business_items = BorrowerBusinesses.objects.filter(borrower__id = borrower.id)
            loan_items = Loan.objects.filter(borrower__id = borrower.id)
            for item in business_items:
                if item.sector == "FOOD_DRINK":
                    item.sector = "Food & Drink"
                elif item.sector == "PRO_SERVICE":
                    item.sector = "Professional Services"
                elif item.sector == "RETAIL":
                    item.sector = "Retail"
                elif item.sector == "ENTERTAINMENT":
                    item.sector = "Entertainment"

            for item in loan_items:
                item.deletable = True
                item.editable = False
                if item.status == "u":
                    item.status = "Under review"
                    item.editable = True
                elif item.status == "a":
                    item.status = "Approved"
                    item.deletable = False
                elif item.status == "r":
                    item.status = "Rejected"

            return render_to_response('index.html', {"user": request.user, "borrower": borrower,
                                                  "business_items": business_items, "loan_items": loan_items})
        except Borrower.DoesNotExist:
            return render_to_response('index.html', {"user": request.user})
    else:
        return render_to_response('index.html', {"user": request.user})

