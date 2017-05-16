import os

for (path, dir, files) in os.walk("/home/certis/tmp"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        print path, filename, ext
