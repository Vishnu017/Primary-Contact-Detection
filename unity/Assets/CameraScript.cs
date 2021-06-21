using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;


public class CameraScript : MonoBehaviour
{
    
    sendimg ig;
    static WebCamTexture backCam;

    void Start()
    {
        ig = GameObject.FindWithTag("sendimg").GetComponent<sendimg>();
        Debug.Log(Application.persistentDataPath);

        if (backCam == null)
            backCam = new WebCamTexture();

        GetComponent<Renderer>().material.mainTexture = backCam;

        if (!backCam.isPlaying)
            backCam.Play();

    }

    void Update()
    {

    }

    IEnumerator TakePhoto()  // Start this Coroutine on some button click
    {

        // NOTE - you almost certainly have to do this here:

        yield return new WaitForEndOfFrame();

        // it's a rare case where the Unity doco is pretty clear,
        // http://docs.unity3d.com/ScriptReference/WaitForEndOfFrame.html
        // be sure to scroll down to the SECOND long example on that doco page 

        Texture2D photo = new Texture2D(backCam.width, backCam.height);
        photo.SetPixels(backCam.GetPixels());
        photo.Apply();

        //Encode to a PNG
        byte[] bytes = photo.EncodeToPNG();


        File.WriteAllBytes(Application.persistentDataPath + "/"+ "photo0.png", bytes);

        ig.startrout();
        //Write out the PNG. Of course you have to substitute your_path for something sensible
        //    File.WriteAllBytes("D:\\project\\camera\\Assets\\New folder\\photo0.png", bytes);
        //  File.WriteAllBytes("C: \\Users\\User\\Desktop\\New folder\\photo1.png", bytes);
        fileCounter++;
    }

    public void RoutineWrap()
    {
        StartCoroutine(TakePhoto());
    }



   
}