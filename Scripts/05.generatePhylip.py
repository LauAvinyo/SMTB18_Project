import sys

files = sys.argv[1:]
for file_name in files:
    name = file_name[:-3]

    out = open(name+'inp', 'w')

    print(file_name, file=out)
    print('F', file=out)
    print(name+'fil', file=out)
    print('Y', file=out)
    print('F', file=out)
    print(name+'ntw', file=out)

    out.close()
