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


public class namesub : MonoBehaviour
{
    public InputField ip;
    // Start is called before the first frame update
    void Start()
    {
       
    }


    public void senddata()
    {
        PostData();
    }


    [Serializable]
    public class info
    {
        public string name;
        public string sid;
    }

    public void PostData()
    {
        info val = new info();
        val.name = ip.text;
        val.sid = intermediate.shopid;
       
        
        string json = JsonUtility.ToJson(val);
        StartCoroutine(PostRequest("http://192.168.18.5:5000/newinfo", json));
    }

    IEnumerator PostRequest(string url, string json)
    {
        var uwr = new UnityWebRequest(url, "POST");
        byte[] jsonToSend = new System.Text.UTF8Encoding().GetBytes(json);
        uwr.uploadHandler = (UploadHandler)new UploadHandlerRaw(jsonToSend);
        uwr.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        uwr.SetRequestHeader("Content-Type", "application/json");

        //Send the request then wait here until it returns
        yield return uwr.SendWebRequest();

        if (uwr.isNetworkError)
        {
            Debug.Log("Error While Sending: " + uwr.error);
        }
        else
        {
            Debug.Log("Received: " + uwr.downloadHandler.text);
        }
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
