import random
from argparse import ArgumentParser
import sys
import os

class Player:
    '''a class for creating a player for the game
    
    Attributes:
        name(str): players name
        tickets(list of ticket object): a players tickets the are playing with 
        account(int): how much money is in the players account 
    '''
    
    def __init__(self, name):
        '''initializes attributes
        
        Args:
            name(str): players name
        Side Effects:
            sets attributes
        '''
        self.name = name
        self.tickets = []
        self.account = 0
    
    def get_number_tickets(self, budget, ticket_price):
        '''calculates the number of tickets a player can purchase based on their budget
        
        Args:
            budget(int): players price budget
            ticket_price(int): price per ticket 
        Returns:
            num_tickets(int): calculated number of tickets a person can buy 
        '''
        num_tickets = round(budget//ticket_price, 0)
        return num_tickets
    
    def add_ticket(self, num_tickets, game_level):
        '''adds ticket to players ticket list 
        
        Args:
            num_tickets(int): number of tickets a player can have 
            game_level(str): game level player would like per ticket 
        Side Effects:
            populates the tickets attribute 
            
        Navigator: Lily Oakes
        '''
        if len(self.tickets) < num_tickets:
            while True:
                try:
                    if game_level == 'easy':
                        while True:
                            ticket_number = int(input('Choose a number between 0-100: '))
                            if ticket_number in range(0,101):
                                break
                            else:
                                print('please enter number within range 0-100')
                    elif game_level == 'hard':
                        while True:
                            ticket_number = int(input('Choose a number between 0-1000: '))
                            if ticket_number in range(0, 1001):
                                break
                            else:
                                print('please enter number within range 0-1000')
                    break
                except:
                    print('Please enter valid number')
            ticket = Ticket(ticket_number, game_level)
            self.tickets.append(ticket)

    
class Ticket:
    '''class for creating tickets for the lottery game 
    
    Attributes:
        number_selected(int): number the player selected for the ticket
        game_level(str): which game level the ticket is associated with 
    '''
    
    def __init__(self, number_selected, game_level):
        '''initializes attributes
        
        Args:
            number_selected(int): number the player selected for the ticket 
            game_level(str): which game level the ticket is associated with 
        '''
        self.number_selected = number_selected
        self.game_level = game_level
        
    def check_ticket(self, random_number, game_level):
        '''checks how close ticket number is to winning number and calculates prize
        
        Args:
            random_number(int): winning number generated 
            game_level(str): which game level the ticket is associated with 
        Returns:
            prize(int): how much a player won for the ticket 
            
        Driver: Lily Oakes
        '''
        #add to print how many they won and how many they lost
        if game_level == 'easy':
            if self.number_selected == random_number:
                print('You guessed the number correctly!')
                prize = 100
            elif (self.number_selected in range(random_number-5, random_number))or (self.number_selected in range(random_number, random_number+5)):
                print(f'The correct number was {random_number} and you guessed {self.number_selected}. You win $50')
                prize = 50
            elif (self.number_selected in range(random_number-10, random_number))or (self.number_selected in range(random_number, random_number+10)):
                print(f'The correct number was {random_number} and you guessed {self.number_selected}. You win $10')
                prize = 10
            else:
                print(f'You lose. The correct number was {random_number} and you guessed {self.number_selected}')
                prize = 0
        elif game_level == 'hard':
            if self.number_selected == random_number:
                print('You guessed the number correctly!')
                prize = 1000
            elif (self.number_selected in range(random_number-30, random_number))or (self.number_selected in range(random_number, random_number+30)):
                print(f'The correct number was {random_number} and you guessed {self.number_selected}. You win $500')
                prize = 500
            elif (self.number_selected in range(random_number-80, random_number))or (self.number_selected in range(random_number, random_number+80)):
                print(f'The correct number was {random_number} and you guessed {self.number_selected}. You win $100')
                prize = 100
            else:
                print(f'You lose. The correct number was {random_number} and you guessed {self.number_selected}')
                prize = 0
        return prize
    
    def generate_random_number(self, game_level):
        '''generates random winning number 
        
        Args:
            game_level(str): game level associated with ticket 
        Returns:
            random_num(int): winning number 
        '''
        if game_level == 'easy':
            random_num = random.randint(0, 100)
        elif game_level == 'hard':
            random_num = random.randint(0, 1000)
        else:
            raise ValueError("Invalid game level")
        return random_num
        
def main(name, budget):
    '''carries out lottery game 
    
    Args:
        name(str): players name
        budget(int): players price budget for tickets 
        
    Driver: Lily Oakes
    Navigator: Sera Belasco
    '''
    ticket_price = 5
    player = Player(name)
    #print(player.name)
    budget = int(budget)
    #print(budget)
    num_tickets = player.get_number_tickets(budget, ticket_price)
    print(f'You get {num_tickets} tickets')
    ticket_counter = 1
    while ticket_counter <= num_tickets:
        while True:
            game_level = input(f"Enter game level for ticket {ticket_counter} ('easy' or 'hard'): ")
            if game_level == 'easy' or game_level == 'hard':
                break
            else:
                print('please enter valid game level')
        player.add_ticket(num_tickets, game_level)
        ticket_counter+=1
    os.system('cls||clear')
    for ticket in player.tickets:
        random_num = ticket.generate_random_number(ticket.game_level)
        result = ticket.check_ticket(random_num, ticket.game_level)
        player.account+=result
    print(f"Thanks for playing {player.name}! You won {player.account} dollars")
        
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables name and budget.
    """
    parser = ArgumentParser()
    parser.add_argument("name", type=str, help="players name")
    parser.add_argument("budget", type=int, help="players budget for tickets")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    main(arguments.name, arguments.budget)
