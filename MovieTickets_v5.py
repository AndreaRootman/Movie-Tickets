"""Movie theater ticket system -v4
Update totals
created by Andrea Rootman
"""


# component 4 - confirm order
def confirm_order(ticket, number, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"\nYou have ordered {number} {ticket} ticket(s)"
                        f" at a cost of ${cost * number:.2f\}\n"
                        f"('Y' or 'N': ").upper()
        if confirm == 'Y':
            return True

        else:
            return False


#component 3 - Calculate ticket price
def get_price(type_):
    prices = [["A", 12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price in [0] == type:
            return price[1]



#component 1 - welcome screen and set up variables
def sell_ticket():
    print("********** potato movies - ticketing system ***********\n")

    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    total_tickets = 0


#component 2 - get the category and number of tickets required

ticket_wanted = "Y"
while ticket_wanted == "Y":
    ticket_type = input("What kind of ticket do you want:\n"
                        "\t 'A' for Adult, or \n"
                        "\t 's' for Student, or\n"
                        "\t 'C' for Child, or \n"
                        "\t 'T' for Gift Voucher\n"
                        ">> ").upper()
    num_tickets = int(input(f"How many {ticket_type} tickets do you want:"
                            f""))
    cost = get_price(ticket_type)

    if confirm_order(ticket_type, num_tickets, cost):
        print("Order confirmed")

        # component 5 - update totals
        total_sales += cost
        tickets_sold += num_tickets
        if ticket_type == "A":
            adult_tickets += num_tickets
        elif ticket_type == "S":
            student_tickets += num_tickets
        elif ticket_type == "C":
            child_tickets += num_tickets
        else:
            gift_tickets += num_tickets


    else:
        print("Order cancelled")


    ticket_wanted = input("Do you want  to sell another ticket? (Y/N): "
                          "").upper()


#main routine
sell_ticket()