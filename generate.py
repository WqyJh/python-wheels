import os
import io
from jinja2 import Environment, FileSystemLoader, select_autoescape


def find_libs():
    return {
        d: [f for f in os.listdir(d) if f.endswith('.whl')]
        for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')
    }


def render():
    libs = find_libs()

    env = Environment(
        loader=FileSystemLoader(os.path.curdir),
        autoescape=False
    )
    template = env.get_template('template.html')

    html = template.render({
        'libs': libs,
    })
    return html


if __name__ == '__main__':
    html = render()

    with io.open('index.html', 'w') as f:
        f.write(html)
