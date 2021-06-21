using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.Networking;


public class assignstatus : MonoBehaviour
{
    public Text statustext;
    // Start is called before the first frame update
    void Start()
    {
        statustext.text = intermediate.status;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
