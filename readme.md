

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

I slutet av min funktion för att skapa en kortlek så behöver jag en funktion som returnerar den skapade och blandade kortleken och därför anväder jag "return deck" så att jag kan använda mig kortlek i resten av programmet för att dela ut kort till mig och dealern. 






