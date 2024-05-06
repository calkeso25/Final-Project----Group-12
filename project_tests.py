import project1


#Testing the ticket class

def test_ticket():
  ticket1 = Ticket(5, 'easy')
  assert project1.check_ticket(5) == 'You guessed the number correctly!'

#Testing the person class

def test_person():
  person1 = Person('test_person') 
  assert person1.get_number_tickets(20, 4) == 5
  person1.add_ticket(4, 'easy')
  assert len(person1.tickets) == 4

#Testing the main function
