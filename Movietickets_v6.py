"""Movie theater ticket system -v6
Print end summary
created by Andrea
"""


# component 6 - print summary
def print_summary(tickets_sold, adult_tickets, student_tickets, child_tickets, gift_tickets, total_sales):
    print("="*20)
    print(f"The total tickets sold today was {tickets_sold}\n"
          f"This was made up of: \n"
          f"\t{adult_tickets} for adults; and\n"
          f"\t{student_tickets} for students; and\n"
          f"\t{child_tickets} for children; and\n"
          f"\t{gift_tickets} gift vouchers \n")
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


#component 2 - get catwgory and number of tickets required

ticket_wanted = "Y"
while ticket_wanted == "Y":
    ticket_type = input("What kind of ticket do you want:\n"
                        "\t 'A' for Adult, or \n"
                        "\t 's' for Student, or\n"
                        "\t 'C' for Child, or \n"
                        "\t 'G' for Gift Voucher\n"
                        ">> ").upper()
    num_tickets = int(input(f"How many {ticket_type} tickets do you want:"
                            f""))
    cost = get_price(ticket_type)

    if confirm_order(ticket_type, num_tickets, cost):
        print("Order confirmed")

# component 5 - Update totals
        total_tickets += cost * num_tickets
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
#component 6 - produce summary of sales
print_summary("tickets_sold, adult_tickets, student_tickets, child_tickets, gift_tickets, total_sales")



#main routine
sell_ticket()
print("Goodbye\nThanks for using Potato Movies")
