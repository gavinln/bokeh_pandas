from __future__ import print_function

import os
import csv

import xml.etree.ElementTree as ET
#from itertools import izip


def here():
    return os.path.abspath(os.path.dirname(__file__))


def getPolygonPoints(xmlPolygonStr):
    ''' returns lists of x and y coordinates which are in turn
        lists of lists
    '''
    root = ET.fromstring(xmlPolygonStr)
    xs = []
    ys = []
    for element in root.findall('.//coordinates'):
        xs_ = []
        ys_ = []
        pointSets = element.text.split(' ')
        for pointSet in pointSets:
            values = [float(value) for value in pointSet.split(',')]
            xs_.append(values[0])
            ys_.append(values[1])
        xs.append(xs_)
        ys.append(ys_)

    return (xs, ys)


def getPolygons(csvFile):
    boundaries = []
    names = []
    with open(csvFile, 'rb') as csvfile:
        mapReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for idx, row in enumerate(mapReader):
            if idx > 0:
                name = (row[0], row[1])
                names.append(name)
                boundaries.append(row[3])
    return boundaries, names


def main():
    programDir = os.path.join(here(), '..', 'data')
    dataFileName = 'US Regions State Boundaries.csv'
    dataFile = os.path.join(programDir, dataFileName)
    boundaries, names = getPolygons(dataFile)
    xs = []
    ys = []

    for idx, name in enumerate(names):
        print(idx, name)

    for idx, boundary in enumerate(boundaries):
        print(names[idx])
        xs_, ys_ = getPolygonPoints(boundary)
        xs.append(xs_)
        ys.append(ys_)

    return [xs, ys, names]

if __name__ == '__main__':
    main()
