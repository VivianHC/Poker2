# -*- coding: UTF-8 -*-
import random
import os
import codecs
def create_deck(new_deck):
    '推出一副新牌'
    print('\n---debug:I made a new deck.---')
    cardJokers = ('♛', '♕')
    cardMarks = ('♠', '♥', '♦', '♣')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')
    for c in cardJokers:
        new_deck.append(c)
    for cn in cardNumbers:
        for cm in cardMarks:
            card = cm + cn
            new_deck.append(card)
    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'
    print('\n---debug:I shuffled a deck.---')
    random.shuffle(deck_to_be_shuffled)
    return


def record_deck(deck_to_be_record,filename):
    '记录一副新牌'
    print('\n---debug:I record a deck.---')
    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close
    return
