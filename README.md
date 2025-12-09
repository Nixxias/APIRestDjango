# REST API Biblioteki (Django)

##  Cel i Opis Projektu
Projekt stanowi realizację zadania polegającego na zaprojektowaniu i zaimplementowaniu prostego API RESTowego w technologii **Django** oraz **Django REST Framework (DRF)**. System umożliwia podstawowe operacje CRUD (Create, Read, Update, Delete) na trzech encjach:
* **Autor** (relacja 1:N z książkami)
* **Książka** (relacja 1:N z egzemplarzami)
* **Egzemplarz**

Aplikacja została przygotowana tak, aby przejść rygorystyczną weryfikację przez **automatyczne testy jednostkowe** (dostarczone w formie plików `.js` i `.html`), działające po stronie klienta (przeglądarki).

##  Wymagania Funkcjonalne
Projekt spełnia następujące wymagania specyficzne:
1.  **Struktura danych:**
    * `Książka`: posiada tytuł, rok (nieujemny) i relację do Autora.
    * `Autor`: imię i nazwisko (niepuste).
2.  **Logika biznesowa:**
    * Przy tworzeniu książki autor podawany jest przez ID (`authorId`).
    * Przy pobieraniu książki (GET) zwracany jest pełny, zagnieżdżony obiekt autora.
    * Możliwość filtrowania książek po ID autora (`GET /books?authorId=1`).
3.  **Zgodność z testami:**
    * Specyficzna obsługa kodów HTTP (np. `204 No Content` dla edycji).
    * Obsługa JSON w formacie `camelCase` (`authorId` zamiast `author_id`).
    * Wyłączone wymuszanie ukośników w adresach URL (obsługa ścieżek typu `/books` bez `/` na końcu).

---

##  Instalacja i Konfiguracja

Aby uruchomić projekt lokalnie, wykonaj poniższe kroki.

### 1. Klonowanie i środowisko wirtualne
Zaleca się uruchomienie projektu w izolowanym środowisku.

```bash
# Utworzenie środowiska (Windows)
python -m venv venv
# Aktywacja
venv\Scripts\activate


# Utworzenie środowiska (Linux/Mac)
python3 -m venv venv
# Aktywacja
source venv/bin/activate
```

2. Instalacja zależności
Zainstaluj Django, DRF oraz bibliotekę do obsługi CORS.

```bash
pip install django djangorestframework django-cors-headers
```

3. Konfiguracja plików testowych
Uwaga: Aby testy działały poprawnie i nie były blokowane przez przeglądarkę (CORS/ścieżki względne), pliki testowe muszą znajdować się wewnątrz struktury Django.

Upewnij się, że pliki index.html oraz main.js znajdują się w katalogu: library_project/library/static/

Struktura projektu powinna wyglądać tak:

```bash
library_project/
├── manage.py
├── library_project/
│   ├── settings.py
│   └── ...
└── library/
    ├── models.py
    ├── serializers.py
    ├── views.py
    └── static/           <--- PLIKI TESTOWE  - wrzuć dostarczone osobno main.js i index.html do folderu static - odpowiada za wykonanie testu API rest i oceny poprawności z zadaniem.
        ├── index.html
        └── main.js
```

4. Baza danych
Wykonaj migracje, aby utworzyć strukturę bazy danych (SQLite).

```bash
python manage.py makemigrations
python manage.py migrate
```

Uruchomienie i Testowanie
 
Uruchom serwer:

```bash
python manage.py runserver
```

Uruchom testy: Otwórz przeglądarkę internetową i wejdź na poniższy adres (ważne: użyj linku HTTP, nie otwieraj pliku z dysku!):

```bash
http://127.0.0.1:8000/static/index.html
```

aplikacja może zostać uruchomiona na innym local ip - jeżeli masz inny niż podany wyżej wpisz swój adres, który otrzymałeś w termianlu po uruchomieniu  http://TWÓJ-ADRES-IP/static/index.html

Testy powinny uruchomić się automatycznie. 
