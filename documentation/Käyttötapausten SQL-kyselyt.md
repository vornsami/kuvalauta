Käydään käyttötapausten SQL-kyselyt samassa järjestyksessä, kun ne käydään käyttöohjeessa.

###Etusivu avataan

SELECT * FROM thread

Jokaista saatua ketjua kohden tehdään vielä kyselyt

SELECT * FROM comment WHERE comment.thread_id = ?
SELECT * FROM comment WHERE comment.thread_id = ?
SELECT * FROM image WHERE image.id = ?


###Käyttäjä luo käyttäjätilin

INSERT INTO account (date_created, date_modified, name, username, password, acc_type) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'username', 'username', 'password', 'USER')

Luotuaan käyttäjätilin käyttäjä siirtyy takaisin etusivulle.

###Käyttäjä kirjautuu sisään

SELECT * FROM account WHERE account.username = 'username' AND account.password = 'password'

###Käyttäjä muuttaa muille käyttäjille näkyvää nimeään. 

UPDATE account SET date_modified=CURRENT_TIMESTAMP, name='new_name' WHERE account.id = ?
Käyttäjä antaa käyttäjätunnuksensa ja salasanansa, joten tietokannasta tehdään kirjautumista vastaava kysely.

###Käyttäjä vaihtaa salasanansa

UPDATE account SET date_modified=CURRENT_TIMESTAMP, password='new_password' WHERE account.id = ?
Käyttäjä antaa käyttäjätunnuksensa ja salasanansa, joten tietokannasta tehdään kirjautumista vastaava kysely.

###Käyttäjä poistaa käyttäjätunnuksensa

DELETE FROM account WHERE account.id = ?
Käyttäjä antaa käyttäjätunnuksensa ja salasanansa, joten tietokannasta tehdään kirjautumista vastaava kysely.

###Käyttäjä luo uuden ketjun, johon on liitettynä kuva

SELECT * FROM account WHERE account.id = ?
SELECT * FROM image
INSERT INTO image (date_created, date_modified, name, filename) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'image_name', 'id.fileformat')
SELECT * FROM account WHERE account.id = ?
INSERT INTO thread (date_created, date_modified, title, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Title', ?)
SELECT * FROM account WHERE account.id = ?
SELECT * FROM thread WHERE thread.id = ?
SELECT * FROM image WHERE image.id = ?
INSERT INTO comment (date_created, date_modified, content, account_id, thread_id, image_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'content', ?, ?, ?)

###Käyttäjä avaa ketjun sivun

SELECT * FROM thread WHERE thread.id = ?
SELECT Comment.* FROM Comment WHERE thread_id = ?

Jokaista kommenttia kohden tehdään kyselyt

SELECT * FROM account WHERE account.id = ?
SELECT * FROM image WHERE image.id = ?

###Käyttäjä lisää uuden kommentin ketjuun

SELECT * FROM account WHERE account.id = ? // autorisointi

SELECT * FROM thread WHERE thread.id = ?
SELECT * FROM account WHERE account.id = ?
SELECT * FROM image 
INSERT INTO image (date_created, date_modified, name, filename) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'image_name', 'id.fileformat')
SELECT * FROM account WHERE account.id = ?
SELECT * FROM image WHERE image.id = ?
INSERT INTO comment (date_created, date_modified, content, account_id, thread_id, image_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'content', ?, ?, ?)

###Kommentin poistaminen

SELECT * FROM account WHERE account.id = ? // autorisointi

SELECT * FROM comment WHERE comment.id = ? // hae poistettava kommentti
SELECT * FROM image WHERE image.id = ? // hae poistettava kuva
DELETE FROM image WHERE image.id = ? // poista kuva
DELETE FROM comment WHERE comment.id = ? // poista kommentti

###Ketjun poistaminen

SELECT * FROM account WHERE account.id = ? // autorisointi

SELECT * FROM thread WHERE thread.id = ?
SELECT * FROM comment WHERE comment.thread_id = ?

Jokaiselle kommentille:

SELECT * FROM image WHERE image.id = ? // hae poistettava kuva
DELETE FROM image WHERE image.id = ?
DELETE FROM comment WHERE comment.id = ?

Lopuksi:

DELETE FROM thread WHERE thread.id = ?
