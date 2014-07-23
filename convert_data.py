import codecs

encoded = codecs.open('initial_data_utf8.json', 'r', 'utf-8').read().encode(
            'ascii', 'backslashreplace')
out = open('initial_data.json', 'w')
for c in encoded:
    out.write(chr(c))