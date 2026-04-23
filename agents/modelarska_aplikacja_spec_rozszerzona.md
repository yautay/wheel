# Modelarska aplikacja do mieszania kolorów
## Rozszerzona specyfikacja produktu i architektury

## 1. Cel produktu

Aplikacja webowa typu desktop-first dla modelarzy, służąca do pracy na własnych farbach, własnych paletach i własnych recepturach. Produkt ma pomagać w praktycznych decyzjach warsztatowych, a nie udawać laboratoryjnej dokładności.

Główne zastosowania:
- dobieranie mieszanek z farb, które użytkownik realnie posiada
- dobieranie rozjaśnień pod efekt skali
- generowanie modulacji koloru wokół koloru bazowego
- zapisywanie palet, receptur i projektów modelarskich
- później: pobieranie koloru z kamery i korekta na podstawie próbki

## 2. Założenia projektowe

- Aplikacja ma być webowa, wygodna na dużym ekranie.
- Backend: FastAPI + Python.
- Frontend: Vue 3 + TypeScript + Pinia + Tailwind.
- Baza na start: SQLite.
- Logowanie użytkownika obowiązkowe.
- Wszystkie dane są przypisane do użytkownika.
- Logowanie aplikacyjne przez Loguru.
- Kolor liczony wewnętrznie w przestrzeni LAB / LCH, nie wyłącznie w RGB.
- UI ma używać dużego, segmentowego koła kolorów, nie płynnego gradientu.

## 3. Główne moduły produktu

### 3.1 Auth i konto użytkownika
Zakres MVP:
- rejestracja
- logowanie
- wylogowanie
- refresh token
- pobranie danych zalogowanego użytkownika
- zmiana hasła po zalogowaniu

Zakres późniejszy:
- reset hasła przez email
- weryfikacja email
- remember me
- podstawowy rate limit dla auth

### 3.2 Moje farby
Każda farba użytkownika powinna mieć:
- markę
- linię produktową
- kod
- nazwę
- typ farby
- wykończenie
- notatki
- kolor referencyjny
- wartości LAB
- status posiadania
- opcjonalnie tagi

Przykładowe statusy:
- owned
- empty
- wishlist

### 3.3 Palety
Paleta to logiczny zbiór farb i/lub relacji tonalnych.
Przykłady:
- Pantera late war
- Olive drab highlights
- IJN greys
- Skóra figurek

Funkcje:
- tworzenie palety
- dodawanie farb do palety
- oznaczanie ról w palecie, np. base, highlight, shadow, modifier
- duplikacja palety
- zapis komentarzy

### 3.4 Receptury
Receptura opisuje wynik działania jednego z trybów aplikacji.
Powinna zawierać:
- nazwę
- tryb
- kolor docelowy
- kolor przewidywany
- użyte farby
- proporcje
- notatki
- opcjonalne oznaczenie jako sprawdzona

### 3.5 Projekty
Projekt agreguje dane związane z konkretnym modelem.
Powinien zawierać:
- nazwę projektu
- typ modelu
- skalę
- notatki
- przypisane palety
- przypisane receptury

### 3.6 Silnik koloru
Wspólny rdzeń dla trzech trybów:
- mixing
- scale effect
- modulation

## 4. Trzy tryby aplikacji

### 4.1 Tryb 1: Mixing
Cel:
Użytkownik wybiera kolor docelowy oraz zestaw posiadanych farb, a aplikacja proponuje mieszankę.

Wejście:
- target color
- lista farb
- opcjonalne ograniczenia: max składników, bez bieli, bez czerni, tylko z palety

Wyjście:
- główna propozycja mieszanki
- 2–3 alternatywy
- przewidywany kolor wyniku
- wskaźnik podobieństwa
- ostrzeżenia

### 4.2 Tryb 2: Scale effect
Cel:
Użytkownik wybiera kolor bazowy oraz preset skali, a aplikacja sugeruje przesunięcie koloru i najlepszy rozjaśniacz z tego, co posiada.

Presety skali:
- 1:35
- 1:48
- 1:72
- 1:144
- 1:350
- 1:700

Dodatkowe style:
- neutral
- warm
- cool
- faded
- dusty
- naval

Wyjście:
- kolor po przesunięciu
- najlepsza farba do rozjaśnienia
- alternatywy
- proporcja startowa
- ostrzeżenia o ryzyku kredowości lub utraty tonu

### 4.3 Tryb 3: Modulation
Cel:
Użytkownik wybiera kolor bazowy, a aplikacja generuje 5-stopniową modulację:
-2, -1, base, +1, +2

Dodatkowe ustawienia:
- siła modulacji: subtle, standard, strong
- opcjonalnie typ modelu: armor, aircraft, ship, figure

Wyjście:
- 5 punktów tonalnych
- propozycje mieszanek dla każdego punktu
- najbliższe farby posiadane
- alternatywy

## 5. Segmentowe koło kolorów

Koło jest wspólnym komponentem dla całej aplikacji.

Założenia:
- duże
- segmentowe
- nie płynny gradient
- sterowane pickerem
- zależne od trybu

Konfiguracja MVP:
- 24 segmenty hue
- 5 lub 7 poziomów tonalnych
- render w SVG

Koło powinno umożliwiać:
- wskazanie koloru bazowego
- wskazanie koloru docelowego
- przeciąganie pickera
- wyświetlanie ghost pickera
- overlay punktów modulacji
- overlay pozycji farb użytkownika

## 6. Model danych

### User
- id
- email
- username
- password_hash
- is_active
- created_at
- updated_at

### UserPreferences
- id
- user_id
- default_scale_preset
- default_modulation_strength
- preferred_brands_json
- ui_settings_json

### Paint
- id
- user_id
- brand
- line
- code
- name
- paint_type
- finish
- notes
- color_hex
- lab_l
- lab_a
- lab_b
- stock_status
- is_owned
- created_at
- updated_at

### Palette
- id
- user_id
- name
- description
- created_at
- updated_at

### PalettePaint
- id
- palette_id
- paint_id
- role

### Recipe
- id
- user_id
- mode
- name
- target_hex
- predicted_hex
- target_lab_l
- target_lab_a
- target_lab_b
- predicted_lab_l
- predicted_lab_a
- predicted_lab_b
- notes
- is_verified
- created_at
- updated_at

### RecipeItem
- id
- recipe_id
- paint_id
- proportion

### Project
- id
- user_id
- name
- scale
- project_type
- notes
- created_at
- updated_at

### ProjectPalette
- id
- project_id
- palette_id

### ProjectRecipe
- id
- project_id
- recipe_id

## 7. Backend architecture

Proponowana struktura katalogów:

```text
app/
  main.py
  api/
    v1/
      auth.py
      users.py
      paints.py
      palettes.py
      recipes.py
      projects.py
      color_engine.py
  core/
    config.py
    database.py
    logging.py
    security.py
  models/
    user.py
    paint.py
    palette.py
    recipe.py
    project.py
  schemas/
    auth.py
    user.py
    paint.py
    palette.py
    recipe.py
    project.py
    color_engine.py
  services/
    auth_service.py
    paint_service.py
    palette_service.py
    recipe_service.py
    project_service.py
    color_mix_service.py
    scale_effect_service.py
    modulation_service.py
  repositories/
    user_repository.py
    paint_repository.py
    palette_repository.py
    recipe_repository.py
    project_repository.py
  utils/
    color.py
    lab.py
```

Zasady:
- routery tylko walidują wejście i delegują do serwisów
- serwisy implementują logikę biznesową
- repozytoria obsługują ORM i bazę
- logika kolorów jest wydzielona do usług i utils

## 8. Logowanie i bezpieczeństwo

Wymagania:
- hashowanie haseł
- JWT access token
- JWT refresh token
- owner-based access
- CORS ograniczony do frontendu
- podstawowe logowanie zdarzeń auth
- brak ujawniania nadmiarowych informacji o błędach logowania

## 9. Logowanie aplikacyjne przez Loguru

Wymagania:
- request id
- user id w kontekście gdzie możliwe
- czas wykonania requestu
- osobne pliki logów według kategorii

Proponowane pliki:
- logs/app.log
- logs/auth.log
- logs/color_engine.log
- logs/error.log

## 10. API v1

### Auth
- POST /api/v1/auth/register
- POST /api/v1/auth/login
- POST /api/v1/auth/refresh
- POST /api/v1/auth/logout
- GET /api/v1/auth/me
- POST /api/v1/auth/change-password

### Paints
- GET /api/v1/paints
- POST /api/v1/paints
- GET /api/v1/paints/{id}
- PATCH /api/v1/paints/{id}
- DELETE /api/v1/paints/{id}

### Palettes
- GET /api/v1/palettes
- POST /api/v1/palettes
- GET /api/v1/palettes/{id}
- PATCH /api/v1/palettes/{id}
- DELETE /api/v1/palettes/{id}
- POST /api/v1/palettes/{id}/paints
- DELETE /api/v1/palettes/{id}/paints/{paint_id}

### Recipes
- GET /api/v1/recipes
- POST /api/v1/recipes
- GET /api/v1/recipes/{id}
- DELETE /api/v1/recipes/{id}

### Projects
- GET /api/v1/projects
- POST /api/v1/projects
- GET /api/v1/projects/{id}
- PATCH /api/v1/projects/{id}
- DELETE /api/v1/projects/{id}

### Color engine
- POST /api/v1/color-engine/mix
- POST /api/v1/color-engine/scale-effect
- POST /api/v1/color-engine/modulation

## 11. Frontend architecture

### Stack
- Vue 3
- TypeScript
- Pinia
- Vue Router
- TailwindCSS

### Widoki
- LoginView
- RegisterView
- DashboardView
- PaintsView
- PalettesView
- RecipesView
- ProjectsView
- MixingView
- ScaleEffectView
- ModulationView
- ProfileView

### Store modules
- authStore
- userStore
- paintsStore
- palettesStore
- recipesStore
- projectsStore
- colorEngineStore
- uiStore

### Kluczowe komponenty
- AppShell
- ColorWheel
- ColorWheelMarker
- PaintListPanel
- PaintFormDialog
- PaletteEditor
- RecipeCard
- MixProposalCard
- ScalePresetSelector
- ModulationStrip
- SaveRecipeDialog

## 12. Layout i UX

### Dashboard
- ostatnie receptury
- ostatnie projekty
- szybkie wejście do 3 trybów
- skróty do farb i palet

### Ekran roboczy trybów
Lewa część:
- duże koło kolorów

Prawa część:
- lista farb
- aktywna paleta
- propozycje mieszanki
- ostrzeżenia
- zapis

Dolny lub boczny panel:
- ustawienia trybu
- presety
- ograniczenia solvera

## 13. MVP scope

Do MVP wchodzą:
- auth
- CRUD farb
- CRUD palet
- zapis receptur
- CRUD projektów
- mixing
- scale effect
- modulation
- segmentowe koło kolorów
- zapis danych per user
- logowanie przez Loguru

Poza MVP:
- skanowanie z kamery
- upload zdjęć próbek
- reset hasła przez email
- zaawansowana kalibracja
- uczenie preferencji użytkownika

## 14. Kolejność implementacji

1. Fundament backendu: config, db, logging, auth
2. Modele ORM i migracje
3. Endpointy auth
4. CRUD farb
5. CRUD palet
6. CRUD receptur
7. CRUD projektów
8. Front auth i shell aplikacji
9. Segmentowe koło kolorów
10. Tryb mixing
11. Tryb scale effect
12. Tryb modulation
13. Polishing UI i walidacje

## 15. Zasady jakości

- czytelny kod
- pełne typowanie TypeScript i Python
- brak nadmiernej magii
- rozsądne komentarze
- separacja warstw
- walidacja wejścia
- sensowne nazwy
- przygotowanie pod przyszłą migrację z SQLite do PostgreSQL
