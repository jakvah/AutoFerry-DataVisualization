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
    private int updateInterval = 100; // in frames

    // Start is called before the first frame update
    void Start()
    {
    Debug.Log ("Starting scenario"); 
    
    // Update folder to match your path
    string folder =@"C:\Users\jakob\Documents\NTNU\EiT\Gemini\Gemini-Unity\Assets\Scripts\"; 
   
    string filename = "temp.txt";
    string fullpath = folder + filename;
    string sometext = "- Format [x,y,z] - \n";  
    File.WriteAllText(fullpath, sometext);  
    }

    // Update is called once per frame
    void Update()
    {
        if (Time.frameCount % this.updateInterval != 0) return;

        float x = transform.position.x;
        float y = transform.position.y;
        float z = transform.position.z;

        string folder =@"C:\Users\jakob\Documents\NTNU\EiT\Gemini\Gemini-Unity\Assets\Scripts\"; 
        string sometext = x.ToString() + "," + y.ToString() + "," + z.ToString() + "\n";  
        string filename = "temp.txt";
        string fullpath = folder + filename;
        File.AppendAllText(fullpath, sometext);
    }
}
