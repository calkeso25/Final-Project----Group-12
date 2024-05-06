import project1


#Testing the ticket class

def test_ticket():
  ticket1 = Ticket(503, 'easy')
  assert project1.check_ticket(ticket1, 503) == 100
  assert project1.check_ticket(ticket1, 499) == 50
  assert project1.check_ticket(ticket1, 495) == 10
  assert project1.check_ticket(ticket1, 475) == 0
  ticket2 = Ticket(500, 'hard')
  assert project1.check_ticket(ticket1, 500) == 1000
  assert project1.check_ticket(ticket1, 490) == 500
  assert project1.check_ticket(ticket1, 455) == 100
  assert project1.check_ticket(ticket1, 340) == 0

#Testing the person class

def test_person():
  person1 = Person('test_person') 
  assert person1.get_number_tickets(20, 4) == 5
  person1.add_ticket(4, 'easy')
  assert len(person1.tickets) == 4

#Testing the main function
