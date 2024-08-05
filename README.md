# Workbooks AI Application
Bubble is a full-stack, no-code app buidler, you can build scalable applications with AI-powered no-code development platform, you can connect your app with ChatGPT or Claude. In this project, if you love reading like I do, you may come acrosse countless of workbooks, and to make sure you ace them, you can stay organized, and have them all in your hand. Bubble can help you with that, by gathering the workbooks listed in your favourite book in one place. This application is powered by OpenAI API. Everyhting is done via the UI. Here are the steps to make one for you.

### Step 1: Set the API Connector
1. Install the API Connector
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(2).png?raw=true)
2- Connect it to OpenAI by filling headers by the following
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(3).png?raw=true)
    Make sure to replace `Bearer "YOUR_OPENAI_KEY_KEY"` with you your actual OpenAI key.
    In this particular project, we used one API call, and that is to the Chat Completions Model. It is a POST request and we are posting the following URL: `https://api.openai.com/v1/chat/completions`
    You can change the `max_tokens` variable to make the application more scalable.
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(4).png?raw=true)
    Then click on Reinitialize Call and make sure that the messade_content's type is text.
3- Create a new data type:
    To store the files that are related to each user, you need to create a new data type.
    Navigate through the Data Types and create a new data type (Aka PDFs).
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(11).png?raw=true)
    In the PDFs data type, create a new field `PDF` of type `file` and create another field `content` of type `text`. Create one more for user name `Full name` of type `text`
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(12).png?raw=true)
4- Create the Sign-up page:
    Because we are using the users data, we need to create the sign-up page to get data from users.
    Create a new page and click on componenets, then choose the sign-up page and drag it into the page.
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(13).png?raw=true)
    Click on "Workflow" tab, then "Add a new event" then choose the event "When page is loaded"
    Click on the event to add a new action, choose "ElementActions" and then "Toggle" and choose as element "Popup Sign Up/Log in" so the page is loaded for the vistors.
    Click in the Sign up bottom and click Add Workflow, then click on Add an action -> Account -> Sign the user Up
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(14).png?raw=true)
    
