# IBM i 7.5 RPGLE + DB2 AI-Centric Template

Questo repository è un template enterprise per lo sviluppo su IBM i 7.5, progettato per essere "AI-Ready". Segue un'architettura rigorosa a tre livelli e standard moderni di programmazione.

## 🏗️ Architettura

Il progetto implementa una netta separazione delle responsabilità:

- **`*_repo` (Data Access):** Solo SQLRPGLE. Gestisce le operazioni CRUD e l'accesso diretto a DB2. Proibito `SELECT *`.
- **`*_serv` (Business Logic):** RPGLE. Contiene la logica applicativa, validazioni e orchestrazione.
- **`*_main` (Entry Point):** Programmi principali o API endpoints.
- **`*_t_*` (Testing):** Programmi di test unitario per validare i servizi.
- **`*_h.rpgleinc`:** Header e definizioni di data structure.

## 📁 Struttura Cartelle

- `/qrpglesrc`: Sorgenti RPGLE e SQLRPGLE.
- `/qsqlsrc`: Script DDL per la creazione di tabelle e indici DB2 for i.
- `/qcllesrc`: Programmi CL (Control Language).
- `/qddssrc`: Eventuali sorgenti DDS legacy o Display Files.
- `/.skills`: Configurazioni di comportamento per agenti AI.

## 🛠️ Regole Fondamentali (GEMINI.md)

1. **Modern RPG:** Solo Free-format RPG. Nessun indicatore legacy.
2. **SQL Standard:** Solo query parametrizzate. Ottimizzazione nativa per DB2 for i.
3. **Naming:** I suffissi determinano il ruolo del componente nell'architettura.
4. **AI-Driven:** Il repository include metadati per permettere a LLM (come Gemini) di generare codice perfettamente integrato.

## 🚀 Come iniziare

1. Clona il template.
2. Definisci le tabelle in `/qsqlsrc`.
3. Crea il layer `_repo` per l'accesso ai dati.
4. Implementa la logica in `_serv`.
5. Valida con un test `_t_`.

---
*Powered by Gemini CLI - IBM i Modernization Suite*
"# ibmi-project" 
