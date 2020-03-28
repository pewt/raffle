#!/usr/bin/env python3

# weighted raffle
import json
from random import choice

def expand(entrant):
    expanded = []
    for i in range(0, entrant['tickets']):
        expanded.append(entrant['name'])
    return expanded

def expand_all(entrants):
    expanded = []
    [expanded.extend(expand(e)) for e in entrants]
    return expanded

entrant_fn = 'entrants.json'

with open(entrant_fn, 'r') as fn:
    entrants = json.load(fn)['entrants']

print("Dumping entrants:")
[print("name: {} tickets: {}".format(e['name'], e['tickets'])) for e in entrants]

tickets = expand_all(entrants)

winner = choice(tickets)
print("{} WON!".format(winner.upper()))
