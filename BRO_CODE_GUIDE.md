# Python – vad allt betyder och gör

En svensk uppslagsfil till [Bro Codes Python-kurs](https://www.youtube.com/watch?v=ix9cRaBkVe0). Använd den medan du tittar. När du hör ett ord i videon kan du söka efter det här. Du behöver inte läsa allt eller memorera det i förväg.

**Gör Bro Codes egna övningar i slutet av avsnitten.** Det här dokumentet förklarar bara begreppen och kodraderna.

## Kursens kapitel

Tiderna leder till startpunkten i samma Bro Code-video. De hjälper dig att hitta ett ämne igen.

- **00:00** Första programmet · **05:49** Variabler · **16:05** Typkonvertering · **21:15** Användarinmatning
- **32:42** Madlibs · **37:55** Matte · **51:46** If-satser · **01:00:06** Miniräknare
- **01:05:59** Viktomvandling · **01:09:59** Temperaturomvandling · **01:13:58** Logiska operatorer · **01:21:28** Villkorsuttryck
- **01:27:03** Textmetoder · **01:39:08** Teckenindex · **01:46:35** Formaterad utskrift
- **01:51:55** While-loop · **01:58:53** Ränta-på-ränta · **02:06:28** For-loop · **02:11:33** Nedräkning · **02:17:28** Nästlade loopar
- **02:23:03** Listor, mängder och tupler · **02:38:08** Varukorg · **02:45:21** Tvådimensionella samlingar · **02:53:59** Quiz
- **03:03:27** Dictionaries · **03:11:33** Kioskprogram · **03:19:42** Slumptal · **03:24:16** Gissningsspel · **03:32:37** Sten, sax, påse · **03:42:06** Tärningskast
- **03:52:12** Funktioner · **04:02:50** Standardargument · **04:08:56** Namngivna argument · **04:15:40** `*args` och `**kwargs`
- **04:30:33** Itererbara värden · **04:37:04** Medlemskapstest · **04:45:56** List comprehensions · **04:56:17** Match-case
- **05:02:13** Moduler · **05:08:51** Variablers räckvidd · **05:14:22** `if __name__ == "__main__"`
- **05:23:34** Bankprogram · **05:38:34** Spelautomat · **05:58:45** Kryptering · **06:07:26** Hangman
- **06:32:32 och framåt** Objektorienterad programmering och fler avancerade ämnen.

## Första kodraderna

### `print()` visar något

```python
print("Hej!")
```

`print` betyder ungefär "visa på skärmen". Texten står mellan citationstecken. Parenteserna talar om vad `print` ska visa.

### Variabler sparar värden

```python
name = "Ossian"
print(name)
```

- `name` är variabelns namn.
- `=` sparar värdet till höger i variabeln till vänster.
- `"Ossian"` är text.
- `print(name)` visar det sparade värdet. Här behövs inga citationstecken runt `name`, eftersom det är variabeln vi vill läsa.

Python skiljer på stora och små bokstäver: `name` och `Name` är olika variabler. Skriv vanliga variabelnamn med små bokstäver, och använd `_` mellan ord: `favorite_food`.

### `input()` frågar användaren

```python
name = input("Vad heter du? ")
print(f"Hej {name}!")
```

- `input(...)` visar en fråga och väntar på att du skriver i terminalen.
- `=` sparar svaret i variabeln `name`.
- Texten från `input()` är alltid en sträng från början.
- `f"...{name}..."` kallas f-sträng. Python byter ut `{name}` mot värdet i variabeln.

## Typer: text, heltal och decimaltal

- **Sträng (`str`)** är text, till exempel `"hej"`.
- **Heltal (`int`)** är ett helt tal, till exempel `7`.
- **Decimaltal (`float`)** har decimaler, till exempel `7.5`.
- **Boolean (`bool`)** kan vara `True` eller `False` – sant eller falskt.

`input()` ger text även när du skriver siffror. Om svaret ska användas i matte måste du omvandla det:

```python
age = int(input("Hur gammal är du? "))
price = float(input("Vad kostar den? "))
```

`int(...)` omvandlar till heltal. `float(...)` omvandlar till decimaltal. `str(...)` omvandlar till text. Om du skriver ord där Python väntar sig ett tal får du ett fel – det är normalt när man övar.

## Räknetecken och jämförelser

| Tecken | Betyder | Exempel |
|---|---|---|
| `+` | addera | `2 + 3` blir `5` |
| `-` | subtrahera | `5 - 2` blir `3` |
| `*` | multiplicera | `3 * 4` blir `12` |
| `/` | dividera | `8 / 2` blir `4.0` |
| `//` | heltalsdivision | `9 // 2` blir `4` |
| `%` | resten efter division | `9 % 2` blir `1` |
| `**` | upphöjt till | `2 ** 3` blir `8` |
| `==` | lika med? | `3 == 3` blir `True` |
| `!=` | inte lika med? | `3 != 4` blir `True` |
| `>` / `<` | större / mindre än | `5 > 2` blir `True` |
| `>=` / `<=` | större/mindre än eller lika med | `4 <= 4` blir `True` |

`=` och `==` är olika: ett enkelt likhetstecken **sparar** ett värde; två likhetstecken **jämför** två värden.

## Beslut: `if`, `elif` och `else`

```python
if score >= 90:
    print("Bra jobbat!")
elif score >= 50:
    print("Godkänt")
else:
    print("Försök igen")
```

- `if` testar det första villkoret.
- `elif` betyder ungefär "annars, testa detta villkor".
- `else` körs om inget tidigare villkor stämde.
- Indraget (mellanslagen före `print`) visar vilka rader som hör till villkoret. Använd **Tab** i VS Code.

Villkor blir `True` eller `False`. De styr vilken kod som körs.

### Logiska operatorer

- `and`: båda villkoren måste vara sanna.
- `or`: minst ett av villkoren måste vara sant.
- `not`: vänder sant till falskt eller tvärtom.

Exempel: `age >= 13 and age <= 19` är sant om åldern ligger mellan 13 och 19.

## Text

Text omges av citationstecken. Några vanliga operationer:

- **Sammanfoga:** `"Hej " + name` sätter ihop två textbitar.
- **Metod:** `name.upper()` gör bokstäverna stora; `name.lower()` gör dem små. Punkten betyder att metoden hör till textvärdet `name`.
- **Index:** `word[0]` hämtar första tecknet. Python börjar räkna från noll.
- **Slicing:** `word[0:3]` hämtar en del av texten från index 0 fram till, men inte inklusive, index 3.
- **F-sträng:** `f"Hej {name}"` sätter in värdet från en variabel i text.
- **Formaterat tal:** används för att bestämma hur ett tal visas, till exempel med två decimaler. Följ Bro Codes exempel på format specifiers.

## Loopar: upprepa kod

### `while`

`while` upprepar raderna så länge villkoret är sant. Något i loopen behöver till slut ändra villkoret, annars fortsätter den för alltid.

### `for`

`for` går igenom värden, till exempel alla saker i en lista, eller upprepar något ett bestämt antal gånger.

### Nästlade loopar

En nästlad loop är en loop inuti en annan loop. Den inre loopen körs för varje varv i den yttre. Det används ibland för rader och kolumner.

### `break`, `continue`, `pass`

- `break` avslutar loopen direkt.
- `continue` hoppar till nästa varv.
- `pass` gör ingenting; det kan markera en plats där kod ska läggas till senare.

## Samlingar

### Lista (`list`)

En ordnad samling som kan ändras:

```python
foods = ["pizza", "pasta"]
```

Du kan hämta första värdet med `foods[0]`, lägga till med `.append(...)` och gå igenom listan med en `for`-loop.

### Tuple (`tuple`)

En ordnad samling som vanligtvis inte ändras efter att den skapats. Den skrivs ofta med parenteser: `(10, 20)`.

### Mängd (`set`)

En samling unika värden. Om samma värde läggs till flera gånger behålls bara en kopia. Den har inte samma fasta positioner som en lista.

### Dictionary (`dict`)

En samling där varje värde nås genom en nyckel:

```python
person = {"name": "Ossian", "age": 20}
```

`"name"` och `"age"` är nycklar; `"Ossian"` och `20` är värden. Hämta namnet med `person["name"]`.

### Tvådimensionell samling

En samling inuti en samling, till exempel en lista av rader. Tänk en liten tabell med rad och kolumn.

## Funktioner

En funktion är en namngiven del av ett program som går att använda igen:

```python
def greet(name):
    print(f"Hej {name}!")

greet("Ossian")
```

- `def` börjar en funktion.
- `greet` är funktionens namn.
- `name` är en parameter – ett namn för information funktionen ska få.
- `greet("Ossian")` anropar funktionen; `"Ossian"` är argumentet, det faktiska värdet.
- Indraget visar vilka rader som tillhör funktionen.

`return` skickar ett resultat ut ur funktionen. `print` visar något på skärmen; `return` lämnar tillbaka ett värde så att annan kod kan använda det.

- **Standardargument:** ett värde som funktionen använder om du inte skickar in ett annat.
- **Namngivet argument:** ett argument där du skriver parameterns namn, till exempel `greet(name="Ossian")`.
- **`*args` och `**kwargs`:** sätt att ta emot ett varierande antal argument. Det är ett senare ämne – du behöver inte kunna det i början.

## Övriga begrepp som dyker upp senare

- **Slumptal (`random`):** ett tal som programmet väljer slumpmässigt. `import random` laddar in verktyget som gör detta.
- **Modul:** en Python-fil eller ett bibliotek med kod som går att använda från en annan fil. `import` laddar in den.
- **Scope / räckvidd:** var i programmet en variabel kan användas.
- **`if __name__ == "__main__"`:** ett vanligt sätt att skilja kod som körs direkt från kod som bara importeras.
- **List comprehension:** kort syntax för att skapa en ny lista från en annan samling.
- **Match-case:** ett sätt att välja mellan flera möjliga värden eller fall.
- **Undantag / exception:** ett fel som inträffar medan programmet körs. `try` och `except` kan fånga vissa fel och bestämma vad programmet ska göra.
- **Filhantering:** läsa från eller skriva till filer på datorn.
- **Klass och objekt:** grunder i objektorienterad programmering. En klass beskriver en typ av sak; ett objekt är en skapad sak av den klassen.
- **Attribut:** data som hör till ett objekt. **Metod:** en funktion som hör till ett objekt.
- **Arv:** en klass kan bygga vidare på en annan klass.
- **Polymorfism:** olika slags objekt kan svara på samma sorts anrop på sina egna sätt.
- **Dekorator:** ett verktyg som ändrar eller utökar hur en funktion eller metod fungerar.
- **API:** ett sätt för program att be om information eller tjänster från andra program eller servrar.
- **Tråd (thread):** en väg för en del av programmet att arbeta samtidigt med annan kod.
- **GUI:** ett grafiskt gränssnitt med fönster, knappar och textfält.

## Felmeddelanden och felsökning

- **Syntaxfel:** Python kan inte läsa koden, till exempel på grund av en saknad parentes, ett kolon eller fel indrag.
- **Körtidsfel:** koden startar men något går fel medan programmet körs, till exempel att text används som ett tal.
- **Felsökning:** läs felmeddelandet, titta på den utpekade raden och ändra en sak i taget.

När du kör i VS Code visas frågor och felmeddelanden i terminalen längst ner. Det är normalt att få fel när du lär dig – felmeddelanden är ledtrådar.

## GitHub – vad det gör

VS Code är där du skriver kod. GitHub är en onlinekopia av projektet.

- `git add` väljer ändringar.
- `git commit` sparar dem som en namngiven sparpunkt.
- `git push` skickar sparpunkten till GitHub.

Du behöver inte pusha efter varje övning. Spara på GitHub när ett avsnitt eller projekt är färdigt.
