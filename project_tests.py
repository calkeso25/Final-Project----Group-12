import project1


#Testing the ticket class

def test_ticket():
  ticket1 = Ticket(503, 'easy')
  assert project1.check_ticket(ticket1, 503) == 'You guessed the number correctly!'
  assert project1.check_ticket(ticket1, 499) == 'The correct number was 499 and you guessed 503. You win $10'
  assert project1.check_ticket(ticket1, 495) == 'The correct number was 495 and you guessed 503. You win $10'

#Testing the person class

def test_person():
  person1 = Person('test_person') 
  assert person1.get_number_tickets(20, 4) == 5
  person1.add_ticket(4, 'easy')
  assert len(person1.tickets) == 4

#Testing the main function
