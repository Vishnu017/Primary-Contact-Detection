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

public class assignname : MonoBehaviour
{
    public Text nametext;
    // Start is called before the first frame update
    void Start()
    {
        nametext.text = intermediate.name;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
