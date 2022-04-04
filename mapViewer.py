import numpy as np
import sys
import matplotlib.pyplot as plt

def usage():
    print("USAGE: python mapViewer.py <mapFile> OPTIONAL: <x> <y>")

# Function that draws a square with a value of 50
def square(costMap,row,col,rad):
    for i in range(rad*2):
        for j in range(rad*2):
            reRow = row - rad + i 
            reCol = col - rad + j
            if reRow<0 or reCol <0 or reRow>np.shape(costMap)[0] or reCol>np.shape(costMap)[1]:
                continue
            costMap[reRow,reCol]+=50
    

    return costMap


def locator(file,x,y):
    data = np.load(file)
    channel0 = data['channel0']
    xBounds = data['xBounds']
    yBounds = data['yBounds']
    pixelsPerMeter = data['pixelsPerMeter']

    xWidth = int((xBounds[1] - xBounds[0]) * pixelsPerMeter)
    yWidth = int((yBounds[1] - yBounds[0]) * pixelsPerMeter)

    reMap = np.resize(channel0, (yWidth,xWidth))
    col=int(round(x*pixelsPerMeter))
    row=int(round(y*pixelsPerMeter))

    reMap = square(reMap,row,col,5)

    plt.imshow(reMap)
    plt.colorbar()
    plt.show()

def main(file):
    data = np.load(file)
    channel0 = data['channel0']
    xBounds = data['xBounds']
    yBounds = data['yBounds']
    pixelsPerMeter = data['pixelsPerMeter']

    xWidth = int((xBounds[1] - xBounds[0]) * pixelsPerMeter)
    yWidth = int((yBounds[1] - yBounds[0]) * pixelsPerMeter)
    reMap = np.resize(channel0, (yWidth,xWidth))
    plt.imshow(reMap)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 4 or len(sys.argv) == 3:
        usage()
    elif len(sys.argv) == 4:
        locator(sys.argv[1],float(sys.argv[2]),float(sys.argv[3]))
    else:
        main(sys.argv[1])