
CREATE TABLE image (

        id INTEGER NOT NULL,

        date_created DATETIME,

        date_modified DATETIME,

        name VARCHAR(144) NOT NULL,

        fileformat VARCHAR(10) NOT NULL,
        
        image_data BLOB NOT NULL,

        PRIMARY KEY (id)

)



CREATE TABLE account (

        id INTEGER NOT NULL,

        date_created DATETIME,

        date_modified DATETIME,

        name VARCHAR(20) NOT NULL,

        username VARCHAR(20) NOT NULL,

        password VARCHAR(20) NOT NULL,

        acc_type VARCHAR(15) NOT NULL,

        PRIMARY KEY (id)

)



CREATE TABLE thread (

        id INTEGER NOT NULL,

        date_created DATETIME,

        date_modified DATETIME,

        title VARCHAR(144) NOT NULL,

        account_id INTEGER NOT NULL,

        PRIMARY KEY (id),

        FOREIGN KEY(account_id) REFERENCES account (id)

)




CREATE TABLE comment (

        id INTEGER NOT NULL,

        date_created DATETIME,

        date_modified DATETIME,

        content VARCHAR(5020) NOT NULL,

        account_id INTEGER NOT NULL,

        thread_id INTEGER NOT NULL,

        image_id INTEGER,

        PRIMARY KEY (id),

        FOREIGN KEY(account_id) REFERENCES account (id),

        FOREIGN KEY(thread_id) REFERENCES thread (id),

        FOREIGN KEY(image_id) REFERENCES image (id)

)