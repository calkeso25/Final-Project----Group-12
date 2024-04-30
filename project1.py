import random
from argparse import ArgumentParser
import sys

class Player:
    
    def __init__(self, name):
        self.name = name
        self.tickets = []
    
    def get_number_tickets(self, budget, ticket_price):
        num_tickets = round(budget/ticket_price, 0)
        return num_tickets
    
    def add_ticket(self, num_tickets, game_level):
        if len(self.tickets) < num_tickets:
            ticket_number = int(input('What number would you like to choose?: '))
            ticket = Ticket(ticket_number, game_level)
            self.tickets.append(ticket)
    
    def generate_random_number(self, game_level):
        if game_level == 'easy':
            return random.randint(0, 100)
        elif game_level == 'hard':
            return random.randint(0, 1000)
        else:
            raise ValueError("Invalid game level")

    
class Ticket:
    
    def __init__(self, number_selected, game_level):
        self.number_selected = number_selected
        self.game_level = game_level
        
    def check_ticket(random_number):
        #add to print how many they won and how many they lost
        if self.number_selected == random_number:
            message = ('You win')
        else:
            message = ('You lose')
        print(message)
        return message
        
def main(name, budget):
    player = Player(name)
    #print(player.name)
    budget = int(budget)
    #print(budget)
    ticket_price = 10 
    num_tickets = player.get_number_tickets(budget, ticket_price)
    print(num_tickets)
    ticket_counter = 0
    while ticket_counter < num_tickets:
        game_level = input("Enter game level ('easy' or 'hard') ")
        player.add_ticket(num_tickets, game_level)
        ticket_counter+=1
    for ticket in player.tickets:
        #print(ticket)
        if ticket.game_level == 'easy':
            random_num = random.randint(0,100)
        elif ticket.game_level == 'hard':
            random_num = random.randint(0, 1000)
        Ticket.check_ticket(random_num)
        
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
