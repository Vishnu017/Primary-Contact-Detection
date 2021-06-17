using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class request : MonoBehaviour
{
    void Start()
    {
        // A correct website page.
     /*   StartCoroutine(GetRequest("localhost:5000/quarks"));
        PostData();
        StartCoroutine(GetRequest("localhost:5000/quarks"));
     */
        // A non-existing page.
        //StartCoroutine(GetRequest("https://error.html"));
    }

    public void startrout()
    {
        StartCoroutine(GetRequest("192.168.1.123:5000/quarks"));
        PostData();
        StartCoroutine(GetRequest("192.168.1.123:5000/quarks"));
    }

    IEnumerator GetRequest(string uri)
    {
        using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
        {
            // Request and wait for the desired page.
            yield return webRequest.SendWebRequest();

            string[] pages = uri.Split('/');
            int page = pages.Length - 1;

            if (webRequest.isNetworkError)
            {
                Debug.Log(pages[page] + ": Error: " + webRequest.error);
            }
            else
            {
                Debug.Log(pages[page] + ":\nReceived: " + webRequest.downloadHandler.text);
            }
        }
    }

    [Serializable]
    public class Quark
    {
        public string name;
        public string charge;
    }

    public void PostData()
    {

        Quark gamer = new Quark();
        gamer.name = "Billie Eillish";
        gamer.charge = "10";

        string json = JsonUtility.ToJson(gamer);
        StartCoroutine(PostRequest("192.168.1.123:5000/quarks", json));
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
          /*  string a = uwr.downloadHandler.text;
            //  Debug.Log(a);
            var words = a.Split(new char[] { '[', ']' });
            words[1] = words[1].Replace("{", string.Empty);

            words[1] = words[1].Replace("},", ",");
            string b = words[1];
            var res = b.Split(',');

            Debug.Log(res[8]);
            //Debug.Log(words[1]);

            */
        }
    }
}
/*using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;


public class request : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(GetRequest());
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    IEnumerator GetRequest()
    {
        WWWForm form = new WWWForm();
        form.AddField("myfield", "mydata");


        UnityWebRequest www = UnityWebRequest.Post("http://127.0.0.1:5000/", form);


        yield return www.Send();

        if(www.isError)
        {
            Debug.Log(www.error);
        }
        else
        {
            Debug.Log("form upload complete");
        }
        /*

        using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
        {
            yield return webRequest.SendWebRequest();
            if(webRequest.isNetworkError)
            {
                Debug.Log("error " + webRequest.error);
            }
            else
            {
                Debug.Log(webRequest.downloadHandler.text);
            }

        }

        
    }
}
*/