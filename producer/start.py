from app import create_app
from config import get_settings

if __name__ == '__main__':
    app = create_app()
    settings = get_settings()
    app.run(host=settings.host, port=settings.port, debug=True)
