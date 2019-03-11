# coding:utf-8
import commands

with open('read_file/poem.txt', 'r') as f:
    result = list()
    for line in f.readlines():
        line = line.strip()
        a, b = commands.getstatusoutput('ls ' + line)
        result.append(line)
        result.append(str(a))
        result.append(b)
open('read_file/result-readline.txt', 'w').write('%s' % str('\n'.join(result)))
