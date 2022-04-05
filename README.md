# ninjacar_map
Tools to create .npz map

## mapMaker.py

  Takes a `.txt` file that contains a list of X and Y coordinates and generates a `.npz` map with the same name.

  Usage:
  ```
  USAGE: python mapMaker.py <coordsFile>
  ```
## mapRecorder.py

  Reads the position of the car from the Motion capture software and records it into a specified `.txt` file.
  
  ```
  sed 's/alec_parkour/<name-of-car>/' mapRecorder.py
  ```
  Note: To be able to receive the pose from the MoCap system one must first connect to it.
  ```
  roslaunch vrpn_client_ros sample.launch server:=tracker
  ```

  Usage:
  ```
  USAGE: python mapRecorder.py <mapOutputFile>
  ```
## mapViewer.py

  Displays the map that has been obtained by the `mapMaker.py` script. Good for verification/debugging.
  
  Usage:
  ```
  "USAGE: python mapViewer.py <mapFile> OPTIONAL: <x> <y>"
  ```
  The x and y coordiantes will display a circle in those coordinates.
  
