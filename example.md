## Setting Up (Skip)

Use `psql -U postgres` and enter the password.

Look at databases with `\l`. 

Create a database with `CREATE DATABASE CISE;`.

You can delete with `DROP DATABASE CISE`, but don't do that.
 
---

## Example Usage

Connect to database with `\c cise`.

## Create one table

Create the majors table. 

```sql
CREATE TABLE majors(
cip_code VARCHAR PRIMARY KEY,
name VARCHAR
);
```

## Stuck? 

Type `help`. Choose help. (`\?` for psql commands and `\h` for sql help)

## Quit

Type `\q`.
