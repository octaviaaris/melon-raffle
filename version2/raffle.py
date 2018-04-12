"""Randomly pick customer and print customer info"""

from random import choice
from customers import get_customers_from_file

customers = get_customers_from_file("customers.txt")


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print "Tell {name} at {email} that they've won.".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )


def run_raffle():
    """Run the weekly raffle."""

    pick_winner(customers)

run_raffle()
