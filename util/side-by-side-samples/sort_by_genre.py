import glob
from shutil import copyfile
import os
fnames = glob.glob('check-imgs/*')
genres = []

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

for fname in fnames:
    sg = fname[fname.index('/')+1:findnth(fname, "_", 1)]
    style = sg[:sg.rindex('_')]
    genre = sg[sg.rindex('_')+1:]
    if not genre in genres and not genre.startswith("_") and not len(genre)==0:
        genres.append(genre)

for sg in genres:
    os.mkdir('sorted-by-genre/' + sg)
    for f in fnames:
        if sg in f:
            l = f[f.rindex('/')+1:f.index('_.')].split("_")
            q = l[0] + "_" + l[2]
            if not q.startswith("_"):
                copyfile(f, 'sorted-by-genre/' + sg + '/' + q + '.jpeg')