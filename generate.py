import os
import io
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
        loader=FileSystemLoader(os.path.curdir),
        autoescape=False
    )

def find_libs():
    return {
        d: [f for f in os.listdir(d) if f.endswith('.whl')]
        for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')
    }


def render_index(libs):
    template = env.get_template('index_template.html')

    html = template.render({
        'libs': libs,
    })
    return html


def render_lib(lib, files):
    template = env.get_template('lib_template.html')

    html = template.render({
        'lib': lib,
        'files': files,
    })
    return html


if __name__ == '__main__':
    libs = find_libs()
    
    index = render_index(libs)

    with io.open('index.html', 'w') as f:
        f.write(index)

    for lib, files in libs.items():
        html = render_lib(lib, files)

        with io.open('%s/index.html' % lib, 'w') as f:
            f.write(html)
