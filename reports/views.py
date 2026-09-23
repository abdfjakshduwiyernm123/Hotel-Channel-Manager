from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .calculations import calculate_the_report
from .models import Expense, Income


class Views:
    @staticmethod
    @login_required
    def managers_report(request: HttpRequest) -> HttpResponse:
        managers = request.user.groups.filter(name="Managers")
        income = Income.objects.first()
        income_total = income.total_income()
        expense = Expense.objects.first()
        expense_total = expense.total_expense()
        gop, base_fee, incentive_fee, remaining = calculate_the_report(
            income_total, expense_total
        )
        if managers:
            return HttpResponse(
                f"gop = {gop} || base fee = {base_fee} || incentive fee = {incentive_fee} || remaining = {remaining}"
            )
        else:
            return render(request, "reports/access_denied_manager.html")

    @staticmethod
    @login_required
    def owners_report(request: HttpRequest) -> HttpResponse:
        owners = request.user.groups.filter(name="Owners")
        income = Income.objects.first()
        income_total = income.total_income()
        expense = Expense.objects.first()
        expense_total = expense.total_expense()
        gop, base_fee, incentive_fee, remaining = calculate_the_report(
            income_total, expense_total
        )
        if owners:
            return HttpResponse(
                f"GOP = {gop} || Base Fee = {base_fee} || Incentive Fee  = {incentive_fee} || Remaining = {remaining}"
            )
        else:
            return render(request, "reports/access_denied_owner.html")

    @staticmethod
    def home_page(request: HttpRequest) -> HttpResponse:
        return render(request, "reports/home_page.html")
