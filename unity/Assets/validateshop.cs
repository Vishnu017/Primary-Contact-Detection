using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class validateshop : MonoBehaviour
{
    public InputField pass;
    public InputField sid;
    public Text txt;
    //then drag and drop the Username_field


    // Start is called before the first frame update
    void Start()
    {

    }


    public void validate()
    {
        txt = GetComponentInChildren<Text>();
        txt.text = sid.text;
        Debug.Log(txt.text);
        intermediate.shopid = sid.text;
      if(pass.text=="123")
        {
        SceneManager.LoadScene("SampleScene");
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
