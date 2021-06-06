import pygame
import sys
import time

pygame.init()

black = (0,0,0)

gameDisplay = pygame.display.set_mode((1400,1000))
gameDisplay.fill(black)

hoeheHand = 100
hand_x = 200
hand_y = hoeheHand
brad = 15
zeit = time.time()

ballBreite = 10

hoehevirtuelleHand = 700
virtuelleHand_x = 700
virtuelleHand_y = hoehevirtuelleHand

SpielfeldStart = 200
SpielfeldEnde = 1200

Invertierung = 1 # 1=keine; -1= Invertierung
loslassen = 1 #variable, dass nur ein klick Zaehlt und nicht mehrere bei Mouse Button Down ausgefuehrt werden

virtuellerReferenzwert= SpielfeldStart + 500
virtuellerReferenzwert_y=hoehevirtuelleHand

handReferenzwert = SpielfeldStart + 500
handReferenzwert_y = hoeheHand
Faktor = (SpielfeldEnde - virtuellerReferenzwert) / (virtuellerReferenzwert - SpielfeldStart)
pygame.mouse.set_visible(True)

schriftgroesse = 30
font = pygame.font.SysFont('Consolas', schriftgroesse)
farbeHand = (255, 255, 0)

def zeichnen():
    gameDisplay.fill(black)


    pygame.draw.circle(gameDisplay, farbeHand, (hand_x, hand_y), brad, 0) #Hand/Controller
    pygame.draw.line(gameDisplay, (150,0,0), (SpielfeldStart, hoeheHand), (SpielfeldEnde, hoeheHand)) #obere Linie
    pygame.draw.circle(gameDisplay, farbeHand, (virtuelleHand_x, virtuelleHand_y), brad, 0) #virtuelle Hand
    pygame.draw.line(gameDisplay, (150, 0, 0), (SpielfeldStart, hoehevirtuelleHand), (SpielfeldEnde, hoehevirtuelleHand)) #untere Linie
    pygame.draw.circle(gameDisplay, (150,0,0), (virtuellerReferenzwert, virtuellerReferenzwert_y), 10, 0) #virtueller Referenzwert
    pygame.draw.circle(gameDisplay, (150,0,0), (handReferenzwert, handReferenzwert_y), 10, 0) #Hand Referenzwert
    #gruene Kreise zum Testen
    #pygame.draw.circle(gameDisplay, (0, 150, 0), (450, virtuellerReferenzwert_y), 10, 0) #linker gruener Kreis
    #pygame.draw.circle(gameDisplay, (0, 150, 0), (950, virtuellerReferenzwert_y), 10, 0) #rechter gruener Kreis


    pygame.display.update()


while True:
    pygame.time.wait(1)
    zeichnen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if loslassen:
            if 300 < hand_x < 1100 and 300 < virtuelleHand_x < 1100: #Sicherheitsabstand zum Rand, damit es keine zu großen Faktoren werden
                loslassen = 0
                Invertierung *= -1
                virtuellerReferenzwert = virtuelleHand_x
                handReferenzwert = hand_x
                print(Invertierung)
                print(Faktor)


    if event.type == pygame.MOUSEBUTTONUP:
        loslassen = 1

    if event.type == pygame.MOUSEMOTION:
        mPosition = pygame.mouse.get_pos()

        if mPosition[0] < 200:
            hand_x = SpielfeldStart
        elif mPosition[0] > 1200:
            hand_x = SpielfeldEnde
        else:
            hand_x = mPosition[0]
        Abstand = hand_x - handReferenzwert
        if Invertierung == 1:
            Faktor1 = (virtuellerReferenzwert-SpielfeldStart) / (handReferenzwert - SpielfeldStart)
            Faktor2 = (SpielfeldEnde-virtuellerReferenzwert) / (SpielfeldEnde-handReferenzwert)
        else:
            Faktor2 = (virtuellerReferenzwert - SpielfeldStart) / (SpielfeldEnde - handReferenzwert)
            Faktor1 = (SpielfeldEnde - virtuellerReferenzwert) / (handReferenzwert - SpielfeldStart)
        if hand_x < handReferenzwert:
            virtuelleHand_x = virtuellerReferenzwert + Abstand * Invertierung * Faktor1
        if hand_x > handReferenzwert:
            virtuelleHand_x = virtuellerReferenzwert + Abstand * Invertierung * Faktor2






