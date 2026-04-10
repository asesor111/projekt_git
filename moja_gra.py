import pygame
import sys
import random

# Inicjalizacja Pygame
pygame.init()

# Stałe – wymiary okna
SZEROKOSC = 900
WYSOKOSC = 800

# Kolory (R, G, B)
CZARNY = (0, 0, 0)
NIEBIESKI = (0, 0, 255)
ZLOTY = (255, 215, 0)
BIALY = (255, 255, 255)

# Okno gry
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Złap ją!!")

# Zegar (kontrola liczby klatek)
zegar = pygame.time.Clock()

# --- Gracz (prostokąt) ---
gracz_x = SZEROKOSC // 2 - 30
gracz_y = WYSOKOSC - 70
gracz_szer = 100
gracz_wys = 10
szybkosc_gracza = 5

# --- Spadający obiekt (gwiazdka = koło) ---
gwiazdka_x = random.randint(20, SZEROKOSC - 20)
gwiazdka_y = 0
gwiazdka_rozmiar = 20
gwiazdka_szybkosc = 4

# --- Wynik ---
wynik = 0
czcionka = pygame.font.Font(None, 36)

# Główna pętla gry
while True:
    # ----- Obsługa zdarzeń -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ----- Sterowanie (klawisze strzałek) -----
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gracz_x > 0:
        gracz_x -= szybkosc_gracza
    if keys[pygame.K_RIGHT] and gracz_x < SZEROKOSC - gracz_szer:
        gracz_x += szybkosc_gracza

    # ----- Aktualizacja świata -----
    gwiazdka_y += gwiazdka_szybkosc

    # Sprawdzenie kolizji (czy gracz złapał gwiazdkę)
    if (gracz_x < gwiazdka_x + gwiazdka_rozmiar and
        gracz_x + gracz_szer > gwiazdka_x and
        gracz_y < gwiazdka_y + gwiazdka_rozmiar and
        gracz_y + gracz_wys > gwiazdka_y):
        wynik += 1
        gwiazdka_y = 0
        gwiazdka_x = random.randint(20, SZEROKOSC - 20)
        # Zwiększanie trudności co 5 punktów
        if wynik % 5 == 0:
            gwiazdka_szybkosc += 0.5

    # Jeśli gwiazdka spadła poniżej krawędzi – koniec gry
    if gwiazdka_y > WYSOKOSC:
        print(f"Koniec gry! Twój wynik: {wynik}")
        pygame.quit()
        sys.exit()

    # ----- Rysowanie wszystkiego -----
    ekran.fill(CZARNY)                     # tło
    pygame.draw.rect(ekran, NIEBIESKI, (gracz_x, gracz_y, gracz_szer, gracz_wys))   # gracz
    pygame.draw.circle(ekran, ZLOTY, (int(gwiazdka_x + gwiazdka_rozmiar/2), int(gwiazdka_y + gwiazdka_rozmiar/2)), gwiazdka_rozmiar//2)  # gwiazdka
    tekst = czcionka.render(f"Wynik: {wynik}", True, BIALY)
    ekran.blit(tekst, (10, 10))

    # Odświeżenie ekranu
    pygame.display.flip()
    zegar.tick(60)   # 60 klatek na sekundę