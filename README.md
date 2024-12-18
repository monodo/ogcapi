# ogcapi
Experimental projet for managing geographic data with Django ORM and OGC-APIF

## Start dem with dev setup

Clone this repository

```bash
cp env.example .env
docker compose build
docker compose up -d && docker compose logs -f web
```

Migrations and demo data population will be run automatically in DEV mode, including DB flush. Don't try this on production DB...

OGC-APIF endpoints are here ```http://localhost:8001/oapif```
