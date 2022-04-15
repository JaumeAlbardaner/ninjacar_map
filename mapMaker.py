import numpy as np
import sys
from scipy import ndimage

pixelsPerMeter = 100
margin = 3. # Meters of margin in the costmap
# trackWidth = 3 # Three meters 



def usage():
    print("USAGE: python mapMaker.py <coordsFile>")


def main(coordsFile):

    # Read coords file
    with open(coordsFile,'r') as f:
        coords = f.read().split('\n')[:-1]

    # Prepare variables 
    xMin = 999
    yMin = 999
    xMax = -999
    yMax = -999
    
    # First look at the data
    for i in range(len(coords)):
        coords[i] = map(float, coords[i].split(', '))

        if(coords[i][0]>xMax):
            xMax = coords[i][0]
        if(coords[i][1]>yMax):
            yMax = coords[i][1]

        if(coords[i][0]<xMin):
            xMin = coords[i][0]
        if(coords[i][1]<yMin):
            yMin = coords[i][1]

    xMin = xMin - margin
    yMin = yMin - margin
    xMax = xMax + margin
    yMax = yMax + margin

    # Generate the empty map
    rows = int(((yMax - yMin) * pixelsPerMeter))
    cols = int(((xMax - xMin) * pixelsPerMeter))
    channel0 = channel1 = channel2 = channel3 = \
        np.zeros((rows, cols), dtype = np.float32)
    
    # Draw the path
    for i in range(len(coords)):
        x =  int(((coords[i][0] - xMin) * pixelsPerMeter))
        y =  int(((coords[i][1] - yMin) * pixelsPerMeter))
        channel0[y,x] = 1.
    
    # Dilate it to form the distance from every point to the path
    tmpMat1 = channel0
    tmpMat2 = np.zeros(np.shape(channel0))

    while not np.array_equal(tmpMat1, tmpMat2):
        tmpMat2 = tmpMat1
        tmpMat1 = ndimage.binary_dilation(tmpMat1).astype(tmpMat1.dtype)
        channel0 = np.add(channel0,tmpMat1)

    channel0 = channel0 / pixelsPerMeter

    # Invert the points so the closest to the line have the least weight
    currentMax = np.amax(channel0)
    channel0 = channel0 - currentMax
    channel0 = np.absolute(channel0)

    # Truncate the closest points to form a nice track
    # tmp = channel0 <= trackWidth

    # for i in range(np.shape(channel0)[0]):
    #     for j in range(np.shape(channel0)[1]):
    #         if tmp[i][j]:
    #             channel0[i][j] = 0
    
    # Save the data in the expected configuration
    channel0 = np.resize(channel0, (1,rows*cols))
    channel1 = np.resize(channel1, (1,rows*cols))
    channel2 = np.resize(channel2, (1,rows*cols))
    channel3 = np.resize(channel3, (1,rows*cols))


    np.savez(coordsFile[:-4]+".npz", \
    pixelsPerMeter=np.array([pixelsPerMeter], dtype=np.float32),\
    xBounds=np.array([xMin,xMax], dtype=np.float32),\
    yBounds=np.array([yMin,yMax], dtype=np.float32),\
    channel0=channel0,channel1=channel1,channel2=channel2,channel3=channel3)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    else:
        main(sys.argv[1])
