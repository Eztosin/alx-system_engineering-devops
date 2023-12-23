### 0x14-mysql

- First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
  - MySQL distribution must be 5.7.x
  - Make sure that task #3 of your SSH project is completed for
    web-01 and web-02. The checker will connect to your servers to
    check MySQL status
  - Please make sure you have your README.md pushed to GitHub

- Create a database named tyrell_corp.
  - Within the tyrell_corp database create a table named nexus6 and
    add at least one entry to it.
  - Make sure that holberton_user has SELECT permissions on your
    table so that we can check that the table exists and is not empty

- Write a Bash script that generates a MySQL dump and creates a
  compressed archive out of it.
  Requirements:
  - The MySQL dump must contain all your MySQL databases
  - The MySQL dump must be named backup.sql
  - The MySQL dump file has to be compressed to a tar.gz archive
  - This archive must have the following name format:
    day-month-year.tar.gz
  - The user to connect to the MySQL database must be root
  - The Bash script accepts one argument that is the password used
    to connect to the MySQL database
