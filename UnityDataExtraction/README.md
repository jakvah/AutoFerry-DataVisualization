This folder contains source code for extracting and adding data from the Unity simulator to a SQL database.

``GetPositionData.cs`` extracts position data from all 3 boats in the simulation and saves it to a .txt file in realtime.

``GetPositionData.py`` reads through the .txt file in realtime and adds the data 

Note: The user must update the folder PATH in both ``GetPositionData.cs`` and ``GetPositionData.py`` to match the path to the Unity Script folder on their own system. Also, remember to attatch ``GetPositionData.cs`` to the boat object in the Unity Simulator.  