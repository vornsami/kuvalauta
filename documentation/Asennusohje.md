Sovelluksen tulisi toimia paikallisesti asentamalla riippuvuudet ja suorittamalla run.py.


### Yksityiskohtaisemmin:

Asenna python

Pura sovellus haluaamaasi kansioon

Siirry kansioon komentokehotteessa komennolla "cd ohjelman/polku/tähän"

Asenna venv komennolla "py -m venv venv"

Käynnistä venv komennolla "venv\Scripts\activate"

Asenna riippuvuudet komennolla "pip install -r requirements.txt"

Käynnistä ohjelma komennolla "run.py"

Mene selaimessa osoitteeseen http://127.0.0.1:5000/


### Sovelluksen mukauttaminen:

Sovellusta voi mukauttaa avaamalla "application"-kansiossa olevan tiedoston "__init__.py"
Tiedostosta voi muuttaa seuraavien kenttien arvoja vaikuttamatta ohjelman toimintaan:

UPLOAD_FOLDER määrittelee, minne ohjelma tallettaa ladatut tiedostot. Kohteen sijainti on suhteellinen "application"-kansioon. 
Huomaa, että polku tulee olla ympäröitynä lainausmerkeillä.

THREAD_LIMIT määrittelee, kuinka monta ketjua voi olla olemassa kerrallaan, ennen kuin sovellus alkaa niitä automaattisesti poistamaan. 
Sen arvo on pelkkä numero.

DEFAULT_ADMIN_USERNAME määrittelee oletusarvoisen käyttäjänimen automaattisesti luotavalle ADMIN-tason käyttäjälle.
Käyttäjänimi tulee ympäröidä lainausmerkeillä.

DEFAULT_ADMIN_PASSWORD määrittelee oletusarvoisen salasanan automaattisesti luotavalle ADMIN-tason käyttäjälle.
Salasana tulee ympäröidä lainausmerkeillä.

### Heroku


Sovellus toimii herokussa antamalla sille ympäristömuuttuja HEROKU komennolla


heroku config:set HEROKU=1


ja lisäämällä herokuun tietokanta komennolla


heroku addons:add heroku-postgresql:hobby-dev
