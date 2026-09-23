from django.db import models


class Income(models.Model):
    month = models.DateField()
    room_revenue = models.DecimalField(max_digits=12, decimal_places=2)
    food_and_beverage = models.DecimalField(max_digits=12, decimal_places=2)
    other_income = models.DecimalField(max_digits=12, decimal_places=2)

    def total_income(self):
        """
        This methord returns the total room_revenue; food_and_beverage; other_income to calculate total income.
        """
        return self.room_revenue + self.food_and_beverage + self.other_income

    def __str__(self):
        """
        This methord returns the month's income.
        """
        return f"Date = {self.month.strftime('%B %Y')} | Total = {self.total_income()}"


class Expense(models.Model):
    month = models.DateField()
    salaries = models.DecimalField(max_digits=12, decimal_places=2)
    rent = models.DecimalField(max_digits=12, decimal_places=2)
    water = models.DecimalField(max_digits=12, decimal_places=2)
    ota_commissions = models.DecimalField(max_digits=12, decimal_places=2)
    maintenance = models.DecimalField(max_digits=12, decimal_places=2)
    other_costs = models.DecimalField(max_digits=12, decimal_places=2)

    def total_expense(self):
        return (
            self.salaries
            + self.rent
            + self.water
            + self.ota_commissions
            + self.maintenance
            + self.other_costs
        )

    def __str__(self):
        return f"Date = {self.month.strftime('%B %Y')}  | Total Expense = {self.total_expense()}"


class Documents(models.Model):
    document = models.FileField(upload_to=".bills")
    month = models.DateField()

    def __str__(self):
        return f"Date = {self.month.stftime('%B %Y')}"
