# Imports
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.api.main:app",
        host="localhost",
        port=8000,
        ssl_certfile="certs/localhost.pem",
        ssl_keyfile="certs/localhost-key.pem",
        reload=True
    )
