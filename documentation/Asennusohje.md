Sovelluksen tulisi toimia paikallisesti asentamalla riippuvuudet ja suorittamalla run.py.


### Yksityiskohtaisemmin:

Asenna python

Pura sovellus haluaamaasi kansioon

Siirry kansioon komentokehotteessa komennolla "cd ohjelman/polku/t�h�n"

Asenna venv komennolla "py -m venv venv"

K�ynnist� venv komennolla "venv\Scripts\activate"

Asenna riippuvuudet komennolla "pip install -r requirements.txt"

K�ynnist� ohjelma komennolla "run.py"

Mene selaimessa osoitteeseen http://127.0.0.1:5000/


### Sovelluksen mukauttaminen:

Sovellusta voi mukauttaa avaamalla "application"-kansiossa olevan tiedoston "__init__.py"
Tiedostosta voi muuttaa seuraavien kenttien arvoja vaikuttamatta ohjelman toimintaan:

UPLOAD_FOLDER m��rittelee, minne ohjelma tallettaa ladatut tiedostot. Kohteen sijainti on suhteellinen "application"-kansioon. 
Huomaa, ett� polku tulee olla ymp�r�ityn� lainausmerkeill�.

THREAD_LIMIT m��rittelee, kuinka monta ketjua voi olla olemassa kerrallaan, ennen kuin sovellus alkaa niit� automaattisesti poistamaan. 
Sen arvo on pelkk� numero.

DEFAULT_ADMIN_USERNAME m��rittelee oletusarvoisen k�ytt�j�nimen automaattisesti luotavalle ADMIN-tason k�ytt�j�lle.
K�ytt�j�nimi tulee ymp�r�id� lainausmerkeill�.

DEFAULT_ADMIN_PASSWORD m��rittelee oletusarvoisen salasanan automaattisesti luotavalle ADMIN-tason k�ytt�j�lle.
Salasana tulee ymp�r�id� lainausmerkeill�.

### Heroku


Sovellus toimii herokussa antamalla sille ymp�rist�muuttuja HEROKU komennolla


heroku config:set HEROKU=1


ja lis��m�ll� herokuun tietokanta komennolla


heroku addons:add heroku-postgresql:hobby-dev
