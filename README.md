# ninjacar_map
Tools to create .npz map. Created for the implementation of [MPPI](https://github.com/JaumeAlbardaner/mppi_trainer) on the NinjaCar platform.

## Procedure

In order to generate the map correctly, one must follow the following procedure:

1.  Write the topic where the vehicle's pose is being published in line [#11](https://github.com/JaumeAlbardaner/ninjacar_map/blob/2d0fabd5f96feab6e83b38484bd0f6b4312cea13/mapRecorder.py#L11) of `mapRecorder.py`.

2. Ensure the space the vehicle will be moving around is in x-y coordinates (check mocap software).

3. Run commands: 

  ```
  python mapRecorder.py N03
  python mapMaker.py N03.txt
  python mapViewer.py N03.npz
  ``` 
_(These were ran in python2, but if it has to be run in python3, the `map`function that returns an error must be turned into a list)_

----

### mapRecorder.py

  Reads the position of the car from the Motion capture software and records it into a specified `.txt` file.
  
  Usage:
  ```
  USAGE: python mapRecorder.py <mapOutputFile>
  ```
  _Note: To be able to receive the pose from the MoCap system one must first connect to it._
  ```
  roslaunch vrpn_client_ros sample.launch server:=tracker
  ```
  ----
### mapMaker.py

  Takes a `.txt` file that contains a list of X and Y coordinates and generates a `.npz` map with the same name.

  Usage:
  ```
  USAGE: python mapMaker.py <coordsFile>
  ```

  -----
### mapViewer.py

  Displays the map that has been obtained by the `mapMaker.py` script. Good for verification/debugging.
  
  Usage:
  ```
  "USAGE: python mapViewer.py <mapFile> OPTIONAL: <x> <y>"
  ```
  The x and y coordiantes will display a circle in those coordinates.
  
