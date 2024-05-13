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
            
        Driver: Lily Oakes
        Navigator: Sera Belasco
        '''
        num_tickets = round(budget//ticket_price, 0)
        return num_tickets
    
    def create_ticket(self, game_level): 
        '''creates a ticket for player  
        
        Args:
            game_level(str): game level player would like per ticket 
        Side Effects:
            creates a ticket object  

        Driver: Sera Belasco
        Navigator: Lily Oakes
        '''
        while True:
            try:
                #gets ticket number by asking user input to enter a number;
                #also checks that number they selected is in correct range
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
        return ticket
    
    def add_ticket_to_player(self, ticket):
        '''adds ticket objects to players ticket attribute
        
        Args:
            ticket(ticket object): ticket object to add to attribute 
        Side Effects:
            populates players ticket attribute
            
        Driver: Sera Belasco
        Navigator: Lily Oakes
        '''
        self.tickets.append(ticket)
    
    def count_wins_and_losses(self):
        '''Count the number of wins and losses for the player's tickets.
         Returns:
            tuple: A tuple containing the counts of wins and losses.
        Driver: Kesi Harford
        Navigator: Lily Oakes
        '''
        wins = 0
        losses = 0
        for ticket in self.tickets:
            if ticket.prize > 0:
                wins += 1
            else:
                losses += 1
        return wins, losses
    
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
            prize(int): how much each ticket won
        '''
        self.number_selected = number_selected
        self.game_level = game_level
        self.prize = 0
        
    def check_ticket(self, random_number):
        '''checks how close ticket number is to winning number and calculates prize
        
        Args:
            random_number(int): winning number generated 
            game_level(str): which game level the ticket is associated with 
        Returns:
            prize(int): how much a player won for the ticket 
            
        Driver: Lily Oakes
        Navigator: Sera Belasco
        '''
        #add to print how many they won and how many they lost
        if self.game_level == 'easy':
            if self.number_selected == random_number:
                print('You guessed the number correctly!')
                self.prize = 100
            elif (self.number_selected in range(random_number-5, random_number))or (self.number_selected in range(random_number, random_number+5)):
                print(f'The correct number was {random_number} and you guessed {self.number_selected}. You win $50')
                self.prize = 50
            elif (self.number_selected in range(random_number-10, random_number))or (self.number_selected in range(random_number, random_number+10)):
                print(f'The correct number was {random_number} and you guessed {self.number_selected}. You win $10')
                self.prize = 10
            else:
                print(f'You lose. The correct number was {random_number} and you guessed {self.number_selected}')
                self.prize = 0
        elif self.game_level == 'hard':
            if self.number_selected == random_number:
                print('You guessed the number correctly!')
                self.prize = 1000
            elif (self.number_selected in range(random_number-30, random_number))or (self.number_selected in range(random_number, random_number+30)):
                print(f'The correct number was {random_number} and you guessed {self.number_selected}. You win $500')
                self.prize = 500
            elif (self.number_selected in range(random_number-80, random_number))or (self.number_selected in range(random_number, random_number+80)):
                print(f'The correct number was {random_number} and you guessed {self.number_selected}. You win $100')
                self.prize = 100
            else:
                print(f'You lose. The correct number was {random_number} and you guessed {self.number_selected}')
                self.prize = 0
        return self.prize
    
    def generate_random_number(self, game_level):
        '''generates random winning number 
        
        Args:
            game_level(str): game level associated with ticket 
        Returns:
            random_num(int): winning number 
        Driver: Kesi Harford
        Navigator: Sera Belasco
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
    ticket_price = 10
    player = Player(name)
    budget = int(budget)
    num_tickets = player.get_number_tickets(budget, ticket_price)
    print(f'You get {num_tickets} tickets')
    ticket_counter = 1
    while ticket_counter <= num_tickets:
        #gets game level for each ticket while checking user is entering valid input
        while True:
            game_level = input(f"Enter game level for ticket {ticket_counter} ('easy' or 'hard'): ")
            if game_level == 'easy' or game_level == 'hard':
                break
            else:
                print('please enter valid game level')
        ticket = player.create_ticket(game_level)
        player.add_ticket_to_player(ticket)
        ticket_counter+=1
    os.system('cls||clear') #clear terminal screen
    for ticket in player.tickets:
        random_num = ticket.generate_random_number(ticket.game_level)
        result = ticket.check_ticket(random_num)
        player.account+=result
    winnings = player.count_wins_and_losses()
    print(f"Thanks for playing {player.name}! You won {winnings[0]} game(s) and lost {winnings[1]} game(s). You won {player.account} dollars")
        
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
