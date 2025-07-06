# Cotton Eyed Joe

> Where did he come from?  
> And where did he go??

Joe here will take a URL slug and see if an entry exists in the database. If it does, he'll redirect you to the proper (and current) destination. Now you’ll know where the slug came from - and where it go.

---

## 🛠 Setup
This app expects a PostgreSQL 17 backend. Database connection parameters are pulled from the following environment variables:

```
POSTGRES_USER=some_user
POSTGRES_PASSWORD=some_unsecure_password
POSTGRES_DB=some_database
POSTGRES_HOST=some_db_host
POSTGRES_PORT=your_db_port
DATABASE_URL=redundancy_matters
```

Once the environment is ready, install dependencies and initialize the database:

```
$ pip install -r requirements.txt
$ alembic revision --autogenerate -m "Initial schema"
$ alembic upgrade head
```

You should now have an empty but valid schema. Don’t believe me? Login and see for yourself. Nothing but empty tables just waiting for good times.

## 🚀 Running Locally
### With Gunicorn

```
$ export PYTHONPATH=.
$ gunicorn -w 4 -b 0.0.0.0:8000 app.main:app
```

### With Podman

Make sure you have a .env file in your project root. (It is not tracked by git.)

```
$ podman build --no-cache -t cej:latest .
$ podman run --env-file .env -p 8000:8000 cej:latest
```

## 🧠 Bonus Notes

Alembic is configured but migrations are up to you.

If you're deploying via Kubernetes or similar, ensure .env values are mirrored into your secret store.
