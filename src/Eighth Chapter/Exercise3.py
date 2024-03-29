# Assign to a variable in your program a triple-quoted string that contains your favourite text.
# Write a function which removes all punctuation from the string, breaks the string into a list of words,
# and counts the number of words in your text that contain the letter “e”.
# Your program should print an analysis of the text like this:
# Your text contains 243 words, of which 109 (44.8%) contain an "e".

import string

s = """You look at trees and label them just so,

(for trees are `trees', and growing is `to grow');

you walk the earth and tread with solemn pace

one of the many minor globes of Space:

a star's a star, some matter in a ball

compelled to courses mathematical

amid the regimented, cold, Inane,

where destined atoms are each moment slain.

 

At bidding of a Will, to which we bend

(and must), but only dimly apprehend,

great processes march on, as Time unrolls

from dark beginnings to uncertain goals;

and as on page o'erwitten without clue,

with script and limning packed of various hue,

and endless multitude of forms appear,

some grim, some frail, some beautiful, some queer,

each alien, except as kin from one

remote Origo, gnat, man, stone, and sun.

God made the petreous rocks, the arboreal trees,

tellurian earth, and stellar stars, and these

homuncular men, who walk upon the ground

with nerves that tingle touched by light and sound.

The movements of the sea, the wind in boughs,

green grass, the large slow oddity of cows,

thunder and lightning, birds that wheel and cry,

slime crawling up from mud to live and die,

these each are duly registered and print

the brain's contortions with a separate dint.

 

Yet trees and not `trees', until so named and seen -

and never were so named, till those had been

who speech's involuted breath unfurled,

faint echo and dim picture of the world,

but neither record nor a photograph,

being divination, judgement, and a laugh,

response of those that felt astir within

by deep monition movements that were kin

to life and death of trees, of beasts, of stars:

free captives undermining shadowy bars,

digging the foreknown from experience

and panning the vein of spirit out of sense.

Great powers they slowly brought out of themselves,

and looking backward they beheld the Elves

that wrought on cunning forges in the mind,

and light and dark on secret looms entwined.

 

He sees no stars who does not see them first

of living silver made that sudden burst

to flame like flowers beneath the ancient song,

whose very echo after-music long

has since pursued. There is no firmament,

only a void, unless a jewelled tent

myth-woven and elf-patterned; and no earth,

unless the mother's womb whence all have birth.

 

The heart of man is not compound of lies,

but draws some wisdom from the only Wise,

and still recalls him. Though now long estranged,

man is not wholly lost nor wholly changed.

Disgraced he may be, yet is not dethroned,

and keeps the rags of lordship one he owned,

his world-dominion by creative act:

not his to worship the great Artefact,

man, sub-creator, the refracted light

through whom is splintered from a single White

to many hues, and endlessly combined

in living shapes that move from mind to mind.

Though all the crannies of the world we filled

with elves and goblins, though we dared to build

gods and their houses out of dark and light,

and sow the seed of dragons, 'twas our right

(used or misused). The right has not decayed.

We make still by the law in which we're made.

 

Yes! `wish-fulfilment dreams' we spin to cheat

our timid hearts and ugly Fact defeat!

Whence came the wish, and whence the power to dream,

or some things fair and others ugly deem ?

All wishes are not idle, not in vain

fulfilment we devise - for pain is pain,

not for itself to be desired, but ill;

or else to strive or to subdue the will

alike were graceless; and of Evil this

alone is dreadly certain: Evil is.

 

Blessed are the timid hearts that evil hate,

that quail in its shadow, and yet shut the gate;

that seek no parley, and in guarded room,

through small and bare, upon a clumsy loom

weave rissues gilded by the far-off day

hoped and believed in under Shadow's sway.

 

Blessed are the men of Noah's race that build

their little arks, though frail and poorly filled,

and steer through winds contrary towards a wraith,

a rumour of a harbour guessed by faith.

 

Blessed are the legend-makers with their rhyme

of things nor found within record time.

It is not they that have forgot the Night,

or bid us flee to organised delight,

in lotus-isles of economic bliss

forswearing souls to gain a Circe-kiss

(and counterfeit at that, machine-produced,

bogus seduction of the twice-seduced).

 

Such isles they saw afar, and ones more fair,

and those that hear them yet may yet beware.

They have seen Death and ultimate defeat,

and yet they would not in despair retreat,

but oft to victory have turned the lyre

and kindled hearts with legendary fire,

illuminating Now and dark Hath-been

with light of suns as yet by no man seen.

 

I would that I might with the minstrels sing

and stir the unseen with a throbbing string.

I would be with the mariners of the deep

that cut their slender planks on mountains steep

and voyage upon a vague and wandering quest,

for some have passed beyond the fabled West.

I would with the beleaguered fools be told,

that keep an inner fastness where their gold,

impure and scanty, yet they loyally bring

to mint in image blurred of distant king,

or in fantastic banners weave the sheen

heraldic emblems of a lord unseen.

 

I will not walk with your progressive apes,

erect and sapient. Before them gapes

the dark abyss to which their progress tends -

if by God's mercy progress ever ends,

and does not ceaselessly revolve the same

unfruitful course with changing of a name.

I will not treat your dusty path and flat,

denoting this and that by this and that,

your world immutable wherein no part

the little maker has with maker's art.

I bow not yet before the Iron Crown,

nor cast my own small golden sceptre down.

 

In Paradise perchance the eye may stray

from gazing upon everlasting Day

to see the day-illumined, and renew

from mirrored truth the likeness of the True.

Then looking on the Blessed Land 'twill see

that all is as it is, and yet may free:

Salvation changes not, nor yet destroys,

garden nor gardener, children nor their toys.

Evil it will not see, for evil lies

not in God's picture but in crooked eyes,

not in the source but in the tuneless voice.

In Paradise they look no more awry;

and though they make anew, they make no lie.

Be sure they still will make, not being dead,

and poets shall have flames upon their head,

and harps whereon their faultless fingers fall:

there each shall choose for ever from the All.

"""


def find_es(s):
    s_without_punct = ""
    ecount = 0
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    s_words = s_without_punct.split()
    for word in s_words:
        if word.find("e") > -1:
            ecount += 1
    print((f"Your text contains {len(s_words)} words, " 
           f"of which {ecount} ({round(100*(ecount/len(s_words)),2)}%) contain an 'e'"))


find_es(s)
