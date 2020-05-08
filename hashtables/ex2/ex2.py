#  Hint:  You may not need all of these.  Remove the unused functions.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    ticket_dictionary = {}  # Initialize a dictionary
    route = []  # Initialize a list
    
    for ticket in tickets: # Iterate through the tickets
        ticket_dictionary[ticket.source] = ticket.destination
            
    key = "NONE"
    
    for i in range(1, len(tickets)):
        route.append(ticket_dictionary[key])
        key = ticket_dictionary[key]
    route.append("NONE")
        
    return route
