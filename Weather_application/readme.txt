Pro úspěšnou funkci programu musí být otevřena celá složka ve vývojovém prostředí (testováno ve VS Code)

Program main najde na internetu údaje o počasí na základě uživatelem zadaného města.
Celkem jsou porovnávány 3 různé zdroje dat: OpenWeatherMap, Google Weather a Weather Underground a zjištěná 
data zapíše a uloží do databáze.

Program main2 pracuje po spuštění sám a je nastaven tak, aby každých 10 minut odebral vzorek počasí 
a ten následně zapsal do databáze spolu s časem získání (defaultně je nastaveno město Brno).

U OpenWeatherMap je získávání dat provedeno API metodou, k zapotřebí API klíč
(je součástí složky a nachází se v souboru config.ini).

U zbylých dvou stránek je získávání dat provedeno skrz HTML Session a přístupy k jednotlivým prvkům
web. stránek.

Uživatelské rozhraní je vytvořené pomocí TKinteru a pro zobrazování údajů na ni, jsou použity Label a Canvas.

Databáze pro testování byla použita MySQL a pracoval jsem s ní v porstředí WorkBench.

Program by měl fungovat pro vetšinu měst na světě (odzkoušeno desítky měst z různých zemí světa).
