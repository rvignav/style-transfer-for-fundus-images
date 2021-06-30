import glob
from shutil import copyfile
import os
fnames = glob.glob('check-imgs/*')
styles = []

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

for fname in fnames:
    sg = fname[fname.index('/')+1:findnth(fname, "_", 1)]
    style = sg[:sg.rindex('_')]
    genre = sg[sg.rindex('_')+1:]
    if not style in styles and not style.startswith("_") and not len(style)==0:
        styles.append(style)

for sg in styles:
    os.mkdir('sorted-by-style/' + sg)
    for f in fnames:
        if sg in f:
            try:
                q = f[f.index('_')+1:f.index('_.')]
                if not q.startswith("_"):
                    copyfile(f, 'sorted-by-style/' + sg + '/' + q + '.jpeg')
            except:
                print(f)
                exit(0)