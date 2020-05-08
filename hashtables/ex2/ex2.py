#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtable import (HashTable, put, get)

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
           put(hashtable, ticket.source, ticket.destination) # Put each ticket into the hash table

    current_airport = "NONE"

    for i in range(length):
       route[i] = get(hashtable, current_airport)
       current_airport = route[i]
    
    return route[:-1]
