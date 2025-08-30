import os
from app import create_app

# Agrega estas dos líneas:
from dotenv import load_dotenv
load_dotenv()

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)