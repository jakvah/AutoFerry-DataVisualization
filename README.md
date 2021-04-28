# AutoFerry-DataVisualization
This project aims at visualizing data from the MilliAmpere autoferry, for a control center. As the autoferry currently is not operational, a Unity-based simulator is used to simulate the behaviour of the ferry. This repo contains source code for extrating, saving and visualizing data from the Unity simulator.

### Setup

The scripts for extracting the data from Unity is located in the UnityDataExtraction folder.

``GetPositionData.cs`` extracts position data from all 3 boats in the simulation and saves it to a .txt file in realtime.

``GetPositionData.py`` reads through the .txt file in realtime and adds the data 

Note: The user must update the folder PATH in both ``GetPositionData.cs`` and ``GetPositionData.py`` to match the path to the Unity Script folder on their own system. Also, remember to attatch ``GetPositionData.cs`` to the boat object in the Unity Simulator.  

You must install a SQL database of your choice. Any SQL database should work, but for reference, a MardiaDB database has been used.

Node-RED has been used to send data from the *database* to the Clarify API, and to plot the autoferry on a map, together with other boats in Trondheim (which position has been extracted for Kystverkets AIS API).


**NB**: Make sure to install the required dependencies for both the Python script and Node-RED. These can be found in ```requirements.txt```.
