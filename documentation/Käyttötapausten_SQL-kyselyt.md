Käydään käyttötapausten SQL-kyselyt samassa järjestyksessä, kun ne käydään käyttöohjeessa.


### Huomautuksia


Kaikissa tapauksissa, joissa tässä dokumentissa kirjataan

SELECT * FROM ...

ovat todellisuudessa esimerkiksi Thread-taulussa muodossa

SELECT thread.id AS thread_id, thread.date_created AS thread_date_created, thread.date_modified AS thread_date_modified, thread.title AS thread_title, thread.account_id AS thread_account_id
FROM thread

Päätin muuttaa merkintää, koska tässä tapauksessa kutsuilla ei ole juurikaan eroa, ja lyhyempi merkintä on selkeämpi lukea.



LIMIT ? OFFSET ? -käskyissä on arvoina aina 1 ja 0.




### Otsakkeen lataaminen


Jokaisella sivulla sivusto lataa käyttäjän nimen otsakkeeseen, jolloin tehdään tietokantakutsu

SELECT * FROM account WHERE account.id = ?




### Etusivu avataan


SELECT * FROM thread

Jokaista saatua ketjua kohden tehdään vielä kyselyt


SELECT * FROM comment WHERE comment.thread_id = ? LIMIT ? OFFSET ?

SELECT * FROM comment WHERE comment.thread_id = ? ORDER BY comment.date_created LIMIT ? OFFSET ?

SELECT * FROM image WHERE image.id = ? LIMIT ? OFFSET ?




### Käyttäjä luo käyttäjätilin

SELECT * FROM account WHERE account.name = ? OR account.username = ? LIMIT ? OFFSET ? // Tarkastetaan, onko nimi käytössä

INSERT INTO account (date_created, date_modified, name, username, password, acc_type) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'username', 'username', 'password', 'USER')




### Käyttäjä kirjautuu sisään

SELECT * FROM account WHERE account.username = ? AND account.password = ? LIMIT ? OFFSET ?




### Käyttäjä muuttaa muille käyttäjille näkyvää nimeään. 


SELECT * FROM account WHERE account.username = ? AND account.password = ? LIMIT ? OFFSET ?

SELECT * FROM account WHERE (account.name = ? OR account.username = ?) AND account.id != ? LIMIT ? OFFSET ? // Tarkastetaan, ettei nimi ole kellään muulla käytössä

UPDATE account SET date_modified=CURRENT_TIMESTAMP, name=? WHERE account.id = ?




### Käyttäjä vaihtaa salasanansa


SELECT * FROM account WHERE account.username = ? AND account.password = ? LIMIT ? OFFSET ?

UPDATE account SET date_modified=CURRENT_TIMESTAMP, password=? WHERE account.id = ?





### Käyttäjä poistaa käyttäjätunnuksensa


SELECT * FROM account WHERE account.username = ? AND account.password = ? LIMIT ? OFFSET ?

DELETE FROM account WHERE account.id = ?





### Käyttäjä luo uuden ketjun, johon on liitettynä kuva


SELECT * FROM image

INSERT INTO image (date_created, date_modified, name, filename) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)

SELECT * FROM account WHERE account.id = ?

INSERT INTO thread (date_created, date_modified, title, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Title', ?)

SELECT * FROM account WHERE account.id = ? LIMIT ? OFFSET ?

SELECT * FROM thread WHERE thread.id = ? LIMIT ? OFFSET ?

SELECT * FROM image WHERE image.id = ? LIMIT ? OFFSET ?

INSERT INTO comment (date_created, date_modified, content, account_id, thread_id, image_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'content', ?, ?, ?)

Tietokannasta tämän jälkeen vielä tarkastetaan ketjujen määrä, ja poistetaan ylimääräiset.




### Käyttäjä avaa ketjun sivun


SELECT * FROM thread WHERE thread.id = ? LIMIT ? OFFSET ?

SELECT count(*) AS count_1 FROM (SELECT * FROM comment WHERE comment.thread_id = ?) AS anon_1 // Kommenttien määrä

SELECT Comment.* FROM Comment WHERE thread_id = ?


Jokaista kommenttia kohden tehdään kyselyt


SELECT * FROM account WHERE account.id = ?

SELECT * FROM comment WHERE comment.thread_id = ? ORDER BY comment.date_created LIMIT ? OFFSET ?

SELECT image.filename AS image_filename FROM image WHERE image.id = ? LIMIT ? OFFSET ?


Lopuksi:


SELECT count(*) AS count_1 FROM (SELECT * FROM comment WHERE comment.thread_id = ?) AS anon_1



### Käyttäjä lisää uuden kommentin ketjuun


SELECT * FROM image 

INSERT INTO image (date_created, date_modified, name, filename) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'image_name', 'id.fileformat')

SELECT * FROM account WHERE account.id = ?

SELECT * FROM image WHERE image.id = ? LIMIT ? OFFSET ?

INSERT INTO comment (date_created, date_modified, content, account_id, thread_id, image_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'content', ?, ?, ?)




### Kuvan poistaminen


SELECT * FROM account WHERE account.id = ?

SELECT * FROM commentWHERE comment.id = ? LIMIT ? OFFSET ?

SELECT * FROM imageWHERE image.id = ? LIMIT ? OFFSET ?

UPDATE comment SET date_modified=CURRENT_TIMESTAMP, image_id=? WHERE comment.id = ?

DELETE FROM image WHERE image.id = ?




### Kommentin poistaminen


SELECT * FROM account WHERE account.id = ?

SELECT * FROM comment WHERE comment.id = ? LIMIT ? OFFSET ?

SELECT * FROM image WHERE image.id = ? LIMIT ? OFFSET ?

DELETE FROM image WHERE image.id = ?

DELETE FROM comment WHERE comment.id = ?




### Ketjun poistaminen


SELECT * FROM account WHERE account.id = ?

SELECT * FROM thread WHERE thread.id = ? LIMIT ? OFFSET ?

SELECT * FROM comment WHERE comment.thread_id = ?


Jokaiselle kommentille:


SELECT * FROM image WHERE image.id = ? LIMIT ? OFFSET ?

DELETE FROM image WHERE image.id = ?

DELETE FROM comment WHERE comment.id = ?


Lopuksi:

DELETE FROM thread WHERE thread.id = ?

