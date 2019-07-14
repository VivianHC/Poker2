# -*- coding: UTF-8 -*-
import random
import os
import codecs

from machine.std_mach import create_deck,\
    shuffled_deck,\
    record_deck
from dealer.Mike import deal_to_a_player,deal_to_multi_players
first_deck = []
create_deck(first_deck)
record_deck(first_deck, "deck-001.txt")

shuffled_deck(first_deck)
record_deck(first_deck, "deck_001.txt")
'''
Qitian_deck = []
deal_to_a_player(first_deck, 10, Qitian_deck)
record_deck(Qitian_deck, "Qitian_deck.txt")
Yilei_deck = []
deal_to_a_player(first_deck, 5, Yilei_deck)
record_deck(Yilei_deck, "Yilei_deck.txt")
Woguanni_deck = []
deal_to_a_player(first_deck, 15, Woguanni_deck)
record_deck(Woguanni_deck, "Woguanni_deck.txt")
'''
Qitian_deck=[]
Yilei_deck = []
Woguanni_deck = []
Weiguang_deck = []
deal_to_multi_players(first_deck,Qitian_deck,Yilei_deck,Woguanni_deck,Weiguang_deck)
record_deck(Qitian_deck,"Qitian_deck.txt")
record_deck(Yilei_deck,"Yilei_deck.txt")
record_deck(Woguanni_deck,"Woguanni.txt")
record_deck(Weiguang_deck,"Weiguang.txt")
