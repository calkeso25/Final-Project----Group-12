import random

class Player:
    
    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets
    
    def get_number_tickets(budget, ticket_price):
        num_tickets = round(budget/ticket_price)
        return num_tickets
    
    def add_ticket(num_tickets):
        tickets = 0
        if tickets < num_tickets:
            ticket_number = int(input('What number would you like to choose?: '))
            ticket = Ticket(ticket_number)
            tickets.append(ticket)
            tickets += 1
    
class Ticket:
    
    def __init__(self, number_selected, game_level):
        self.number_selected = number_selected
        self.game_level = game_level
        
    def check_ticket(number_selected, name):
        player = Player(name)
        for ticket in player.tickets:
            if ticket.game_level == 'easy':
                random_num = random.randint(0,100)
            elif ticket.game_level == 'hard':
                random_num = random.randint(0, 1000)
            if number_selected == random_num:
                print('You win')
            else:
                print('You lose')
