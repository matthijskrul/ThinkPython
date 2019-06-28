# Create a list [0..51] to represent an encoding of the 52 cards in a deck.
# Shuffle the cards, slice off the top five as your hand in a poker deal. Display the hand you have been dealt.

import random
import pygame

card_width = 71
card_height = 96
card_list = list(range(52))


class CardSprite:

    def __init__(self, img, posn):
        self.image = img
        self.posn = posn

    def draw(self, cardnumber, x, target_surface):  # where x is 0, 1, 2, 3 for the 4 card sets
        spriterect = ((1 + cardnumber * (card_width + 2)), x*(2 + card_height), card_width, card_height)
        target_surface.blit(self.image, self.posn, spriterect)


def main():
    pygame.init()
    surface_sz = 600
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    cardsheet = pygame.image.load("C:\\Users\Matthijs\Programming\ThinkPython\src\Seventeenth Chapter\windows-playing-cards.png")
    card1 = CardSprite(cardsheet, (100, 500))
    card2 = CardSprite(cardsheet, (175, 500))
    card3 = CardSprite(cardsheet, (250, 500))
    card4 = CardSprite(cardsheet, (325, 500))
    card5 = CardSprite(cardsheet, (400, 500))
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break
        main_surface.fill((0, 200, 255))
        random.shuffle(card_list)
        hand = card_list[0:5]
        card1.draw((hand[0]//4), (hand[0]//13), main_surface)  #first divide for card value, then for set
        card2.draw((hand[1]//4), (hand[1]//13), main_surface)
        card3.draw((hand[2]//4), (hand[2]//13), main_surface)
        card4.draw((hand[3]//4), (hand[3]//13), main_surface)
        card5.draw((hand[4]//4), (hand[4]//13), main_surface)
        pygame.display.flip()
        pygame.time.delay(1000)
    pygame.quit()


main()
