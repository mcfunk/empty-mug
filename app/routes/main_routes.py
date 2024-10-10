from fasthtml.responses import HTMLResponse
from app.services.html_helpers import generate_html, tag

def register_routes(app):
    @app.get("/", response_class=HTMLResponse)
    async def landing_page():
        content = tag('h1', "Welcome to My CRUD App!") + tag('p', "This is the landing page.")
        return generate_html(content)

    @app.get("/create", response_class=HTMLResponse)
    async def create_page():
        content = tag('h2', "Create an Item") + tag('p', "Form goes here...")
        return generate_html(content, "Create")

    @app.get("/read", response_class=HTMLResponse)
    async def read_page():
        content = tag('h2', "Read Items") + tag('p', "List of items goes here...")
        return generate_html(content, "Read")

    @app.get("/update", response_class=HTMLResponse)
    async def update_page():
        content = tag('h2', "Update an Item") + tag('p', "Form for updating items goes here...")
        return generate_html(content, "Update")

    @app.get("/delete", response_class=HTMLResponse)
    async def delete_page():
        content = tag('h2', "Delete an Item") + tag('p', "Form for deleting items goes here...")
        return generate_html(content, "Delete")
