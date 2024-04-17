import random
from argparse import ArgumentParser
import sys

class Player:
    
    def __init__(self, name):
        self.name = name
        self.tickets = []
    
    def get_number_tickets(budget, ticket_price):
        num_tickets = round(budget/ticket_price, 0)
        return num_tickets
    
    def add_ticket(num_tickets, game_level):
        tickets = 0
        if tickets < num_tickets:
            ticket_number = int(input('What number would you like to choose?: '))
            ticket = Ticket(ticket_number, game_level)
            tickets.append(ticket)
            tickets += 1
        return tickets
    
class Ticket:
    
    def __init__(self, number_selected, game_level):
        self.number_selected = number_selected
        self.game_level = game_level
        
    def check_ticket(number_selected, random_number):
        if number_selected == random_number:
            message = ('You win')
        else:
            message = ('You lose')
        print(message)
        return  message
        
def main(name, budget):
    player = Player(name)
    print(player.name)
    budget = int(budget)
    print(budget)
    ticket_price = 10
    num_tickets = player.get_number_tickets(budget, ticket_price)
    print(num_tickets)
    player.add_ticket(num_tickets, 'easy')
    for ticket in player.tickets:
        if ticket.game_level == 'easy':
            random_num = random.randint(0,100)
        elif ticket.game_level == 'hard':
            random_num = random.randint(0, 1000)
        Ticket.check_ticket(ticket.number_seleced, random_num)
        
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables name and budget.
    """
    parser = ArgumentParser()
    parser.add_argument("name", help="players name")
    parser.add_argument("budget", help="players budget for tickets")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    main(arguments.name, arguments.budget)
