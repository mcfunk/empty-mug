from fasthtml import Fasthtml, request
from fasthtml.responses import HTMLResponse
from app.routes import main_routes

app = Fasthtml()

# Register routes
main_routes.register_routes(app)

if __name__ == "__main__":
    app.run()
