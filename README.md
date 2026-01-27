E-commerce Data Pipeline & Analytics (Medallion Architecture)

Ez a projekt egy End-to-End adatfeldolgozási folyamatot mutat be, amely egy fiktív webshop nyers tranzakciós adataiból készít üzleti döntéstámogató riportokat. A projekt a modern adattárház-építésben használt Medallion Architecture elveit követi.


Adat architektúra:
1. Bronze layer:
Nyers adatok beérkeznek az adatbázisba. Ebben az állapotban még tartalmaznak duplikációt, illetve hiányzó adatokat.

2. Silver layer:
Ebben a rétegben történik az adattisztítás:
- Duplikált szűrés: DISTINCT használatával
- Hiányzó érték szűrés: COALESCE használatával pótolunk
- Üzleti szűrés: Csak a sikeres adatokkal dolgozunk, amik 'cancelled' státuszúak, azokkal nem.

3. Gold Layer:
Aggregált riportok része, itt történnek a komplexebb SQL lekérdezések végrehajtása:
- Customer Metrics -> Legértékesebb vásárló, rendelési gyakoriság, elköltött összeg
- Prodcut Analytics -> Termékek bevétele és népszerűségük


Technológiai Stack:
- Python programozási nyelv
- Adatbáis: SQLite
- Könyvtárak: Pandas, SQLAlchemy, Matplotlib


Gyorsindítás:
1. Repo clone
git clone https://github.com/username/project-name

2. Dependenciesek telepítése 
pip install pandas matplotlib sqlalchemy

3. Fő script futtatás
python main.py


Projekt struktúra:
.
├── bronz_trans.py      # Bronz Layer
├── silver_trans.py     # Silver Layer - duplikáció és hibás adat detektálás
├── gold_trans.py       # Gold Layer - fő SQL lekérdezések
├── main.py             # Vizualizálás
└── webshop.db          # Adatbázis

Vizualizálás:
A folyamat végén a szkript automatikusan generál egy összefoglaló grafikont az SQL-ben előkészített adatok alapján, amely megmutatja a cég legértékesebb vásárlóit.
![Legértékesebb vásárlók](customer_revenue.png)


Jövőbeli fejlesztések:
- A lokális adatok helyett egy API használatával az adatok kicserélése, hogy az adatbázis nagyobb és relevánsabb legyen.


Készítette: Molnár Gergő - https://www.linkedin.com/in/gerg%C5%91-moln%C3%A1r-3920b53a7/