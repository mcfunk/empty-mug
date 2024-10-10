def tag(tag_name, content='', **attrs):
    attributes = ' '.join(f'{key}="{value}"' for key, value in attrs.items())
    if attributes:
        return f"<{tag_name} {attributes}>{content}</{tag_name}>"
    return f"<{tag_name}>{content}</{tag_name}>"

def html(content):
    return f"<!DOCTYPE html><html lang='en'>{content}</html>"

def head(title="My CRUD App"):
    return tag('head', 
        tag('meta', charset="UTF-8") +
        tag('meta', name="viewport", content="width=device-width, initial-scale=1.0") +
        tag('title', title) +
        tag('style', """
            body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
            header { background-color: #333; color: white; padding: 1rem 0; }
            header nav ul { list-style: none; display: flex; justify-content: center; padding: 0; margin: 0; }
            header nav ul li { margin: 0 1rem; }
            header nav ul li a { color: white; text-decoration: none; padding: 0.5rem 1rem; }
            header nav ul li a:hover { background-color: #575757; }
        """)
    )

def header():
    nav_items = ''.join([
        tag('li', tag('a', 'Home', href='/')),
        tag('li', tag('a', 'Create', href='/create')),
        tag('li', tag('a', 'Read', href='/read')),
        tag('li', tag('a', 'Update', href='/update')),
        tag('li', tag('a', 'Delete', href='/delete'))
    ])
    nav = tag('nav', tag('ul', nav_items))
    return tag('header', nav)

def footer():
    return tag('footer', tag('p', "&copy; 2024 My CRUD App"))

def body(content):
    return tag('body', header() + tag('main', content) + footer())

def generate_html(content, title="My CRUD App"):
    return html(head(title) + body(content))
