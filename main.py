# -*- coding: iso-8859-1 -*-
import subprocess

words = ['Alice', 'Bob', 'Charles', 'Darwin', 'Elisa', 'Frank', 'Gabriel', 'Hans',
         'Maria', 'isst', 'läuft', 'schwimmt', 'singt', 'rennt', 'schläft', 'tänzt', 'lernt',
         'schnell', 'langsam', 'gut', 'schlecht', 'spät', 'fröhlich', 'früh', 'gemütlich', 'ständig']

for word in words:
    subprocess.call(['espeak', '-v', 'german', '-w',
                     'audios/' + word + '.wav', word])
