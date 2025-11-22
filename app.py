import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Watsonx Orchestrate Agent Demo", layout="wide")

st.title("🤖 Test My Watsonx Orchestrate Agent")

# Embed the Watsonx Orchestrate agent widget
components.html("""
<!DOCTYPE html>
<html>
  <body>
    <div id="root"></div>
    <script>
  window.wxOConfiguration = {
    orchestrationID: "dddbacdbb6c243a3bbe53662be8d492b_7b56ddcd-731f-4711-892f-a4f2577bb280",
    hostURL: "https://eu-gb.watson-orchestrate.cloud.ibm.com",
    rootElementID: "root",
    deploymentPlatform: "ibmcloud",
    crn: "crn:v1:bluemix:public:watsonx-orchestrate:eu-gb:a/dddbacdbb6c243a3bbe53662be8d492b:7b56ddcd-731f-4711-892f-a4f2577bb280::",
    chatOptions: {
        agentId: "e308ae7a-d3d0-4d67-bfc9-cba96a51b7ef", 
    }
  };
  setTimeout(function () {
    const script = document.createElement('script');
    script.src = `${window.wxOConfiguration.hostURL}/wxochat/wxoLoader.js?embed=true`;
    script.addEventListener('load', function () {
        wxoLoader.init();
    });
    document.head.appendChild(script);
  }, 0);                     
</script>
  </body>
</html>
""", height=700, scrolling=True)
