# Database schema

This doc describes the database schema used to run the queries. 

## Articles

| Column | Type                     | Modifiers                                             |
| :----- | :----------------------- | :---------------------------------------------------- |
| author | integer                  | not null                                              |
| title  | text                     | not null                                              |
| slug   | text                     | not null                                              |
| lead   | text                     |                                                       |
| body   | text                     |                                                       |
| time   | timestamp with time zone | default now()                                         |
| id     | integer                  | not null default nextval('articles_id_seq'::regclass) |

### Indexes:

-   `articles_pkey` PRIMARY KEY, btree (id)
-   `articles_slug_key` UNIQUE CONSTRAINT, btree (slug)
-   Foreign-key constraints:
-   `articles_author_fkey` FOREIGN KEY (author) REFERENCES authors(id)    

## Authors

| Column | Type    | Modifiers                                            |
| :----- | :------ | :--------------------------------------------------- |
| name   | text    | not null                                             |
| bio    | text    |                                                      |
| id     | integer | not null default nextval('authors_id_seq'::regclass) |

### Indexes:

-   `authors_pkey` PRIMARY KEY, btree (id)
-   Referenced by:
-   TABLE `articles` CONSTRAINT `articles_author_fkey` FOREIGN KEY (author) REFERENCES authors(id)

## Log

| Column | Type                     | Modifiers                                        |
| :----- | :----------------------- | :----------------------------------------------- |
| path   | text                     |                                                  |
| ip     | inet                     |                                                  |
| method | text                     |                                                  |
| status | text                     |                                                  |
| time   | timestamp with time zone | default now()                                    |
| id     | integer                  | not null default nextval('log_id_seq'::regclass) |

### Indexes:

-   `log_pkey` PRIMARY KEY, btree (id)
