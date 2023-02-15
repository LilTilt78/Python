# Python
Pro úspěšnou funkci programu musí být otevřena celá složka ve vývojovém prostředí (testováno ve VS Code)
- samotný .py soubor nebude fungovat

Program najde na internetu údaje o počasí na základě uživatelem zadaného města.
Celkem jsou porovnávány 3 různé zdroje dat: OpenWeatherMap, Google Weather a Weather Underground

U OpenWeatherMap je získávání dat provedeno API metodou, k zapotřebí API klíč
(je součástí složky a nachází se v souboru config.ini).

U zbylých dvou stránek je získávání dat provedeno skrz HTML Session a přístupy k jednotlivým prvkům
web. stránek.

Uživatelské rozhraní je vytvořené pomocí TKinteru a pro zobrazování údajů na ni, jsou použity Label a Canvas.

Program by měl fungovat pro vetšinu měst na světě (odzkoušeno desítky měst z různých zemí světa).

TO DO:
Projekt by mohl být do budoucna rozšířen o ukládání zjištěných dat
Tato data by mohla být poté přenesena do grafů
