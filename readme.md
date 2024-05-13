

Dokumentation


Jag började med att lära mig lite mer avancerad kod än det vi har lärt oss i porven och under lektionstid för att kunna sammanfatta allting och för att faktiskt kunna lära mig att koda ett blackjack spel med hjälp av python. Här är den videon: https://www.youtube.com/watch?v=mpL0Y01v6tY. Jag kollade även på en lite längre video när jag kom hem efter lektionen: https://www.youtube.com/watch?v=e3YkdOXhFpQ.

Mitt första mål som ska sätta upp för mig själv var att förstå vad koden innebar och inte bara skriva den utan att tänka själv och förstå varför jag gör som jag gör. Därför så spenderade jag denna lektionen till att sitta i ett grupprum och kolla på olika youtube videos som förklarar väldigt bra denna video kollade jag på under lektionen: https://www.youtube.com/watch?v=aryte85bt_M 

Idag är det en ny vecka och jag ska fortsätta med att kolla klart på den gamla yt videon och även kolla på en till efteråt som jag hittade : https://www.youtube.com/watch?v=p15xzjzR9j0

Mitt andra mål inför de kommande veckorna är att börja skriva koden vilket jag började med idag. Jag laddade ner pygame idag för windows så att jag ska kunna visuellt se mina kort och dealerns kort visuellt. Det tog lite längre tid än förväntat då det strulade med nerladdningen och ingeting ville fungera men jag lyckades till slut att lösa det. Jag kopplade pygame med hjälp av (Import pygame) och (Pygame.init) sen hann jag även med att bestäma lite färger och hur stor rutan skulle vara som kom upp när man spelade blackjack i pygame. Jag valde färgerna vit, svart och röd. 

Mitt andra mål för de kommande veckorna var att jag skulle kunna se mina kort och dealerns som man kunde se visuellt på pygame och sen skulle jag även skapa en funktion för att kunna skapa en kortlek. Jag använde mig av cards_images = {}: För att skapa en tom dictionary som kommer användas för att lagra laddade kortbilder som jag kommer lägga in som man kommer att se visuellt i pygame. jag hade väldigt mycket problem med att.

    Efter ett tag och väldigt mycket problem med pygame med att mina bilder på 52 st kort med alla valörer och kläda kort inte kunde hittas "No file '7_of_Clubs.png.jpg' found in working directory 'C:\BlackJack'.
PS C:\BlackJack> " så gav jag upp på pygame, jag satt med min mentor och kenneth i flera lektioner och försökte att lösa det och dom hade också svårt att förstå vad som var fel, vi ändrade om jättemycket i min kod "suits" och ändrade filen från ".png" till ".png.jpg" för att det skulle matcha mina bilder jag laddade ner till pygame. Christoffer la även till lite kod som jag inte riktigt förstod varför han gjorde men han skulle ändra lite värden till "x" och "xy" för att se om det fungerade, hans kod var följande:

x = random.randint(0,3)
        print(x)
        xy = suits[x]
        print(xy)

Christoffers kod löste inte heller problemet och jag fick error message efter error message i flera veckor så jag gav upp på pygame och bestämde mig för att göra en lite simplare blackjack utan något visuellt men så man istället kan välja hit och stand osv och ändå få kort. Det kommer alltså vara ett blackjack utan att man ser det visuellt med korten istället så kommer det upp text.

Här är koden som jag skrev och fick lite hjälp av mina mentorer att skriva från pygame: 

import pygame
import random
import sys

# Initialisera Pygame
pygame.init()

# Färger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Skärmbredd och höjd
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Skapa skärmen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack")

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Ladda kortbilder
cards_images = {}
for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
    for rank in range(2, 11):
        x = random.randint(0,3)
        print(x)
        xy = suits[x]
        print(xy)
        cards_images[f"{rank}_of_{xy}.png"] = pygame.image.load(f"{rank}_of_{xy}.png.jpg")
    for face_card in ['jack', 'queen', 'king']:
        cards_images[f"{face_card}_of_{xy}.png"] = pygame.image.load(f"{face_card}_of_{xy}.png.jpg")
    cards_images[f"ace_of_{xy}.png"] = pygame.image.load(f"ace_of_{xy}.png.jpg")

Trots att detta inte fungerade så har jag ändå lärt mig väldigt mycket om hur man ska koda gällande kortspel och hur själva konceptet ser ut, jag har lärt mig hur helheten fungerar.


Jag började skriva min nya kod med "Import random". Modulen "random" är inbyggd i python och används helt enkelt för att kunna generera tal som är slumpässiga och även listor. Men jag anväder den för att kunna skapa och blanda en kortlek i mitt Blackjack spel. 

För att få mitt spel att fungera så var jag tvungen att skapa en kortlek. För att få det att fungera så använde jag mig av "def create_deck():". Med detta så definerar jag helt enkelt en funktion med namnet "create_deck()". Det denna funktionen gör att det ansvarar för att skapa en ny kortlek. Jag använder även en funktion för att organisera koden och göra den mer läsbar för mig själv. Det tillåter mig även återanvända koden för att skapa en ny kortlek varje gång jag behöver det. En kortlek innehåller 52st kort med 4 olika sviter eller "suits". För att mitt spel ska fungera så skapade jag en lista med alla fyra sviter som finns i en kortlek, "suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']". 

Eftersom att värdet på korten i en kortlek går från 2-A så behövde jag lägga till "ranks" som innehåller alla rankningar från 2-A för att skapa en komplett kortlek. 

Nu har jag kodat in sviterna och dom olika rankingarna av korten för sig men för att det ska bli en komplett kortlek och så att varje svit ska kunna kombineras med varje rank så använder jag mig av "deck = [(rank, suit) for rank in ranks for suit in suits]". Jag kombinerar alltså rankingar och sviter för att repsresentera varje krot i min kortlek. Jag använder detta istället för att använda loppar eller andra metoder för att skapa en kortlek, med hjälp av denna kod så bildas det en slags listkomprehension som är lätt och enkel att förstå. 

Nu när jag har skapat min kortlek så behöver jag något som gör så att den blandas slumpmässigt och därför använder jag "random.shuffle(deck)" för att vara säker på att alla kort är helt blandade och även kommer upp slumpmässigt. 

I slutet av min funktion för att skapa en kortlek så behöver jag en funktion som returnerar min skapade och blandade kortleken och därför anväder jag "return deck" så att jag kan använda min kortlek i resten av programmet för att dela ut kort till mig och dealern. 

Ett av mina mål nu för kommande veckor var att jag behövde skapa en funktion som kunde beräkna mitt värde för varje hand som jag spelade. För att lösa detta så använde jag mig av "def calculate_hand_value(hand):". Sen la jag till 2 st variabler "Value" och "num_aces" och initerade båda till 0. Enkelt förklarat så ger "value" det totala värdet av handen och "num_aces" håller koll på antalet ess i handen vilket är extra viktigt eftersom att ess kan ha värde 1 och 11 beroende på situation i handen. 

För att enkelt förkalra hur funktionen fungerar så kan vi säga att om jag har följade hand, hand = [('A', 'Spades'), ('6', 'Hearts'), ('J', 'Diamonds')] 

Jag börjar med att ge value till 0 och num_aces till 0.
För varje kort i handen:
För det första kortet ('A', 'Spades'):
rank = 'A', eftersom 'A' är den första delen av kortet.
Eftersom rank är 'A', lägger vi jag 11 till value och ökar num_aces till 1.
För det andra kortet ('6', 'Hearts'):
rank = '6'.
Jag lägger till 6 till value.
För det tredje kortet ('J', 'Diamonds'):
rank = 'J'.

Eftersom rank är en klättkort ('J', 'Q', 'K'), lägger jag till 10 till value.
Nu är value 11 (från esset) + 6 (från sexan) + 10 (från klättkortet) = 27.
Jag går sen in i loopen eftersom value är större än 21 och num_aces är 1.
I loopen tar jag bort 10 från value vilket ändrar essets värde från 11 till 1.
value blir nu 17 och num_aces minskas till 0.
Eftersom value nu är 17 som är mindre än 21 och jag inte har fler ess kvar så avslutas loopen.

Nu när jag hade skapat en kortlek och skapat en funktion som kan beräkna värdet för varje hand så behövde jag en funktion som visade mina händer i blackjack, alltså så att när jag kör spelet så ska det komma upp siffror på dealerns hand och min hand. För detta så använder jag mig av "def display_hand(hand, player):" där variablen "hand" ska vara en lista med kort och variabeln  "player" som ska vara namnet på spelarens hand som ska visas. För att printa ut namnet på spelaren som är följt av en f sträng "s Hand:". Jag använder denna strängen för att enkelt kunna inkludera värdet av variabeln "player" i strängen. 

Sen behövde jag skapa en loop som upprepas över varje kort i variablen "hand" och då använde jag "for card in hand:" och sedan "print(card[0])" som i själva loopen skriver ut rangen på varje kort i skärmen enkelt och kort förklarat. 

För att det skulle bli ett logiskt blackjack spel och en huvudfuktion för att spela blackjack som  resten av min kod skulle förstå så skapade jag en funktion med namnet "play_blackjack" och sedan skapade jag en loop funktion där "while" är det själva nyckelordet som innebär att den kommer upprepa ett block av kod så länge ett visst villkor är sant och det är därför jag använder "true". Detta innebär att loopen kommer att forstätta föralltid tills den bryts av ett annat villkor. 
 
 I loopen så skapas det en ny kortlek med "deck = create_deck()" och sedan så delas det ut 2st kort till spelaren och dealern genom att ta bort de två översta korten från kortleken med "player_hand = [deck.pop(), deck.pop()]" och "dealer_hand = [deck.pop(), deck.pop()]".

För att kunna printa ut i och se visuellt vad för kort spelaren och dealern har så använder jag "print (":") , i detta fallet använde jag print"("Dealern hand:") som berättar att följande text kommer att vara information om dealerns hand.

print(dealer_hand[0][0]) använder jag för att här så skrivs det förstsa kortet i dealerns hand ut. Det betyder enkelt förklarat att "dealer_hand" är en lista över kort och varje kort är liksom en lista i sig själv där det första elementet är värdet på kortet och det andra elementet är kortets svit. Detta betyder då att (dealer_hand[0][0]) referar liksom till första kortets värde.

"for card in player_hand:
            print(card[0])". Detta är en for loop som jag skapade för att koden ska kunna gå igenom varje kort i spelarens hand, därför står det "player_hand". Detta betyder att för varje kort så skriver den ut värdet. Detta betyder då "player_hand" är också en lista på kort på samma sätt som det var i "dealer_hand". Och varje kort har ett värde vilket då är det första elementet i dess egen inre lista. 

            Jag insåg efter ett tag av tänkande och en del youtube att jag behöver skapa while loop som tar hand den som spelar varje drag. Alltså där spelaren får välja hit eller stand baserat på vilket värde som korten visar att deras hand är. 

            Fär att detta ska fungera så använde jag mig av "while calculate_hand_value(player_hand) < 21:" som enkelt förklarat kör koden så länge som värdet av spelarens hand är mindre än 21. 

            För att koden ska kunna be spelaren om man vill ta ett kort eller stanna så så behövde den be om en "input" av spelaren. Därför använde jag "action = input ("Do you want to hit or stand? h/s: "). lower()" 

            Sedan behövde jag en kod som utför några funktioner om spelaren väljer att ta ett kort, då använde jag "if action == 'h':". Sedan behövde jag skriva ut vad som sker när spelaren väljer att ta ett kort, player_hand.append(deck.pop()): Ett kort tas från kortleken (deck) med pop() och läggs till i spelarens hand.
            print("Din hand:"): En utskrift som visar att splarens hand kommer att visas.
            Sedan används en for loop för att skriva ut varje kort i spelarens hand.

            Om spelaren väljer att stanna däremot så bryts loopen med "break" eftersom att man inte vill ta fler kort, för detta använde jag "elif action == 's':
                    break". Och om spelaren skulle skriva in något annat än "h" eller "s" så kommer det upp ett felmeddelande tack vare "else" där det står "print("Invalid input! Var snäll och välj 'h' för hit eller 's' för stand.", 
                    " to stand.")". Jag hade väldigt mycket problem med att få denna koden att fungera, det tog lång tid men tillslut fungerade det. 

                    









