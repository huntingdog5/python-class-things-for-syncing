
#for usages testing arepl things
import re
def fileset():
    prmpt = input('enter file name/path:\n')
    #prmpt = input('enter file name/path\n')
    # prmpt = 'mbox-short.txt'
    if prmpt == '':
        filepath = 'mbox-short.txt'
    else:
        try:
            filepath = prmpt
        except:
            print('file cant be opened defaulting to sample file')
            filepath = 'mbox-short.txt'
    return filepath
def re_doer():
    file = open(fileset())
    re_set = input('enter reg expression')
    for line in file:
        line = line.rstrip()
        x = re.findall(re_set, line):
        if len(x) > 0

re_doer()
