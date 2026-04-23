# 🎨 Modelarska Aplikacja do Mieszania Kolorów
## Specyfikacja projektu (Codex 5.3)

---

# 1. CEL PROJEKTU

Aplikacja webowa (desktop-first) dla modelarzy służąca do:

- mieszania kolorów na podstawie posiadanych farb
- symulacji efektu skali
- generowania modulacji kolorów
- zarządzania własnymi farbami, paletami i recepturami

Aplikacja NIE ma być laboratoryjnie dokładna.
Ma być praktycznym narzędziem warsztatowym.

---

# 2. STACK TECHNOLOGICZNY

## Backend
- FastAPI (Python 3.12+)
- SQLAlchemy / SQLModel
- Alembic
- SQLite (MVP)
- Loguru (logowanie)
- JWT (auth)

## Frontend
- Vue 3
- TypeScript
- Pinia
- Vue Router
- TailwindCSS
- SVG (custom color wheel)

---

# 3. GŁÓWNE MODUŁY

## Auth
- rejestracja
- logowanie
- logout
- refresh token

## Paints
- CRUD farb
- HEX + LAB

## Palety
- grupowanie farb

## Receptury
- zapis mieszanek

## Projekty
- powiązanie wszystkiego

---

# 4. TRYBY

## MIX
wejście: farby + target  
wyjście: mieszanka

## SCALE
wejście: kolor + skala  
wyjście: rozjaśnienie

## MODULATION
wejście: kolor  
wyjście: 5 poziomów

---

# 5. API

- POST /auth/login
- GET /paints
- POST /recipes
- POST /color/mix
- POST /color/scale
- POST /color/modulation

---

# 6. UI

- Vue + Pinia + Tailwind
- SVG color wheel

---

# 7. MVP

- login
- farby
- mieszanie
- efekt skali
- modulacja
- zapis

