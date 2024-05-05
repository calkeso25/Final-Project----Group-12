import project1


#Testing the ticket class

def test_ticket():
  ticket1 = Ticket(5, 'easy')
  assert project1.check_ticket(5) == 'You win'

#Testing the person class

def test_person():
  person1 = Person('test_person')
  assert person1.name == 'test_person'

#Testing the main function
