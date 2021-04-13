using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.IO;

public class PositionTest : MonoBehaviour
{
    private int updateInterval = 150; // in frames

    // Start is called before the first frame update
    void Start()
    {
    Debug.Log ("Starting scenario"); 
    // Update folder to match your path
    string folder =@"C:\Users\jakob\Documents\NTNU\EiT\Gemini\Gemini-Unity\Assets\Scripts\"; 
   
    string filename = "temp.txt";
    string fullpath = folder + filename;
    string sometext = "- Format [x,y,z] - HH:mm:ss \n";  
    File.WriteAllText(fullpath, sometext);  
    }

    // Update is called once per frame
    void Update()
    {
        if (Time.frameCount % this.updateInterval != 0) return;

        float x = transform.position.x;
        float y = transform.position.y;
        float z = transform.position.z;
        Debug.Log("Hello");
        string timeString = DateTime.Now.ToString("HH:mm:ss");
        Debug.Log(timeString);

        string folder =@"C:\Users\jakob\Documents\NTNU\EiT\Gemini\Gemini-Unity\Assets\Scripts\"; 
        string sometext = x.ToString() + "," + y.ToString() + "," + z.ToString() + "@" + timeString + "\n";  
        string filename = "temp.txt";
        string fullpath = folder + filename;
        File.AppendAllText(fullpath, sometext);
    }
}
