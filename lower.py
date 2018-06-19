# Change library files' path and filename to lowercase

import shutil
import generate

if __name__=='__main__':
    libs = generate.find_libs()

    for lib, files in libs.items():
        for file in files:
            origin = '%s/%s' % (lib, file)
            after = '%s/%s' % (lib, file.lower())
            shutil.move(origin, after)
        shutil.move(lib, lib.lower())