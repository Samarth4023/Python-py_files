#!/usr/bin/env python
# coding: utf-8

# # While Loops

# In[25]:


# Create a list representing a deck of cards
card_deck = [4, 11, 8, 8, 13, 6, 2, 10]

# Initialize an empty list to represent the player's hand
hand = []

# Keep drawing cards from the deck until the sum of the hand is less than 17
while sum(hand) < 17:
    # Remove the last card from the deck and add it to the hand
    hand.append(card_deck.pop())
    # Print the current hand
    print(hand)


# ### NOTE: The indented body of the loop should modify atleast one variable in the test condition. If the value of the test condition never changes, the result is a infinite loop
