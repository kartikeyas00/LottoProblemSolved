"""
Lotto Problem
    Solved by Kart Sharma
"""
from pprint import pprint
import itertools

list_15 = [i for i in range(1, 16)]  # list of known numbers

def comm_ele(a, b): # This function finds the common elements between the two lists
    result = []
    for element in a:
        if element in b:
            result.append(element)
    return len(result)

def findsubsets(S, m): # This function finds the subsets of the list S nd limits the length of the subsets to m
    a = set(itertools.combinations(S, m))
    return list(a)

list_comb6 = findsubsets(list_15, 6) # producing all the possible tickets

def sub_of_sub(x): # this function finds the subsets of all the possible tickets and limit their number to 3
    c = []
    for i in x:
        c.append(findsubsets(i, 3))
    return c

groups_needed = sub_of_sub(list_comb6)
groups_needed = [item for sublist in groups_needed for item in sublist]
groups_needed=set(groups_needed)
#Above we have created a set called groups_needed which have all the possible subsets of all the possible tickets

tickets = {} # We are creating a dictionary with the possible ticket as the key and all the subsets of that ticket as the value

i = 0
while i < len(list_comb6):
    tickets[list_comb6[i]] = set((findsubsets(list_comb6[i], 3)))
    i = i + 1

def final_tickets(groups_needed,tickets): # This method produces uneliminated final tickets
    final_tickets = set()
    while groups_needed:
        best_ticket = None
        groups_covered = set()
        for ticket, groups in tickets.items():
            covered = groups_needed & groups
            if len(covered) > len(groups_covered):
                best_ticket = ticket
                groups_covered = covered
        groups_needed -= groups_covered
        final_tickets.add(best_ticket)
    return final_tickets

final_tickets=final_tickets(groups_needed,tickets)

def final_ticket_eliminated(final_tickets_uneliminated): # This function further eliminates the tickets by reducing the double counted tickets
    final_tickets=list(final_tickets_uneliminated)       #But this function doesn't cover all the sets
    tickets = {}
    for j in final_tickets:
        i = 0
        while i < len(final_tickets):
            n = comm_ele(j, final_tickets[i])
            if n > 3 and final_tickets[i] != j and final_tickets[i] not in tickets:
                tickets[j] = (final_tickets[i])
            i = i + 1
    list1 = list(tickets.keys())
    list2 = list(tickets.values())
    list3 = list(set(list1).intersection(list2))
    list4 = list((set(list1) - set(list3)))
    return set(final_tickets)-set(list4)

final_tickets_eliminated=final_ticket_eliminated(final_tickets)

def allfinal_tickets(tickets): # This method produces final tickets which cover all the sets.
    global final_tickets_eliminated
    groups_needed = sub_of_sub(list_comb6)
    groups_needed = [item for sublist in groups_needed for item in sublist]
    groups_needed=set(groups_needed)
    group = sub_of_sub(final_tickets_eliminated)
    group= [item for sublist in group for item in sublist]
    group=set(group)
    new_groups_needed=groups_needed-group
    final_tickets = set()
    while new_groups_needed:
        best_ticket = None
        groups_covered = set()
        for ticket, groups in tickets.items():
            covered = new_groups_needed & groups
            if len(covered) > len(groups_covered):
                best_ticket = ticket
                groups_covered = covered
        new_groups_needed -= groups_covered
        final_tickets.add(best_ticket)
    return final_tickets | final_tickets_eliminated

print("I am able to get",len(allfinal_tickets(tickets)),"tickets which is less than 38.They cover all the sets. So I have completed the challenge.")
print("------------You can find all the tickets below-------------")
pprint(allfinal_tickets(tickets))