\# DB2 for i - AI Development Rules (IBM i 7.5)



\## Core principle

All database access MUST be explicit, optimized, and predictable.

Never rely on implicit behavior.



\---



\## SQL usage rules



\### Mandatory rules

\- Always use explicit column lists

\- NEVER use SELECT \*

\- Always use qualified table names

\- Always use explicit JOIN syntax



\---



\## Performance rules (critical on IBM i)



\- Prefer indexed columns in WHERE clauses

\- Avoid full table scans

\- Avoid functions on indexed columns in WHERE

&#x20; ❌ WHERE UPPER(name) = 'X'

&#x20; ✔ WHERE name = ?



\- Use FETCH FIRST n ROWS ONLY instead of LIMIT patterns



\---



\## Transaction control



\- Use commitment control when modifying data

\- Always define isolation level explicitly when needed

\- Group related updates in a single transaction



\---



\## SQL + RPG integration



\- Use EXEC SQL embedded only in SQLRPGLE

\- Never mix native file I/O with SQL on same file

\- Always handle SQLCODE or SQLSTATE



\---



\## Error handling



Mandatory pattern:



EXEC SQL

&#x20; ...

END-EXEC



IF SQLCODE <> 0;

&#x20;  // handle error

&#x20;  // log SQLCODE and SQLSTATE

ENDIF;



\---



\## Security rules



\- Never concatenate user input into SQL strings

\- Always use parameterized queries (host variables)

\- Sanitize external input before SQL usage



\---



\## Modernization rules



When converting legacy RPG:

\- Replace CHAIN/READ with SQL SELECT when possible

\- Replace physical file logic with views

\- Prefer set-based operations over record-by-record loops



\---



\## AI instruction



AI MUST:

\- Optimize queries for DB2 for i (not generic DBMS)

\- Respect IBM i indexing behavior

\- Suggest performance improvements when generating SQLRPGLE

