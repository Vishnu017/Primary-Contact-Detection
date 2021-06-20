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

public class sendimg : MonoBehaviour
{


    void Start()
    {
 
    }

    public void startrout()
    {
        PostData();
    }
   

    [Serializable]
    public class imageinfo
    {
        public string name;
        public string id;
        public string sid;
    }

    public void PostData()
    {
        byte[] imageArray = System.IO.File.ReadAllBytes(Application.persistentDataPath + "/"+ "photo0.png");
        string base64ImageRepresentation = Convert.ToBase64String(imageArray);

        Debug.Log(base64ImageRepresentation);


        imageinfo val = new imageinfo();
        val.name = "image";
        val.id = base64ImageRepresentation;
        val.sid = intermediate.shopid;

        string json = JsonUtility.ToJson(val);
        StartCoroutine(PostRequest("http://192.168.18.5:5000/upload", json));
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
            if(uwr.downloadHandler.text=="False")
            {
                SceneManager.LoadScene("exit");


            }
            else
            {
                intermediate.name = "GOPIKA";
                SceneManager.LoadScene("enter");
            }

        }
    }
 }
