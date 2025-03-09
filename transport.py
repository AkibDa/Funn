import time

class Bus:

  def __init__(self, bus_id, route, total_seats, fare):

    self.bus_id = bus_id
    self.route = route 
    self.total_seats = total_seats
    self.availabe_seats = total_seats
    self.fare = fare 

  def check_availability(self):

    return self.available_seats

  def book_tickets(self, num_seats):

    if num_seats > self.available_seats:
      return False

    self.available_seats -= num_seats
    return True

  def get_fare(self, num_seats):

    return self.fare * num_seats