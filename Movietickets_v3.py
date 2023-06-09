"""Movie theater ticket system -v1
welcome screen and variables
created by Andrea Rootman
"""

#component 3 - Calculate ticket price
def get_price(type):
    prices = [["A", 12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price [0] == type:
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
    print(f"You have ordered {num_tickets} {ticket_type} ticket(s)"
          f" at a cost of ${cost * num_tickets:.2f}!")

    ticket_wanted = input("Do you want  to sell another ticket? (Y/N):"
                          "").upper()



#main routine
sell_ticket()