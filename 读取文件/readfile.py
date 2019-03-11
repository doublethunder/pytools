# coding:utf-8
import commands

with open('poem.txt', 'r') as f:
    result = list()
    for line in f.readlines():
        line = line.strip()
        a, b = commands.getstatusoutput('ls ' + line)
        result.append(line)
        result.append(a)
        result.append(b)
open('result-readline.txt', 'w').write('%s' % '\n'.join(result))
