from fastapi import FastAPI

import sentry_sdk

sentry_sdk.init(
    dsn="https://e0c03f5bef3eab9b70728375a904fad9@o4506200479170560.ingest.sentry.io/4506200481464321",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 2 / 0
