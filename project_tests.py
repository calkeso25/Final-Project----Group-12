import project1


#Testing the ticket class

def test_ticket():
  ticket1 = project1.Ticket(503, 'easy')
  assert ticket1.check_ticket(503) == 100
  assert ticket1.check_ticket(499) == 50
  assert ticket1.check_ticket(495) == 10
  assert ticket1.check_ticket(475) == 0
  ticket2 = project1.Ticket(500, 'hard')
  assert ticket2.check_ticket(500) == 1000
  assert ticket2.check_ticket(490) == 500
  assert ticket2.check_ticket(455) == 100
  assert ticket2.check_ticket(340) == 0

#Testing the person class

def test_person():
  person1 = project1.Player('test_person') 
  assert person1.get_number_tickets(20, 4) == 5
  ticket = project1.Ticket(78, 'easy')
  person1.add_ticket_to_player(ticket)
  assert len(person1.tickets) == 1
  ticket2 = project1.Ticket(320, 'hard')
  person1.add_ticket_to_player(ticket2)
  assert len(person1.tickets)== 2


#Main function is not checked with a unit test because it requires user input
#However, the main function mostly invokes other methods, which are all tested
