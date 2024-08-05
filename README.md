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
    You can be creative as you want for the UI.
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(1).png?raw=true)
    Click on `Workflow` tab, then `Add a new event` then choose the event "When page is loaded"
    Click on the event to add a new action, choose `ElementActions` and then `Toggle` and choose as element `Popup Sign Up/Log in` so the page is loaded for the vistors.
    Click in the Sign up bottom and click Add Workflow, then click on Add an action -> Account -> Sign the user Up 
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(14).png?raw=true)
    Then fill fields with the following: 
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(15).png?raw=true)
    The next step of the workflow is to naviagte the user to another page, create a page new page first in the Design section and then add another action to the workflow -> Navigation -> Go to another Page
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(16).png?raw=true)
5- Upload PDFs page:
    Go to the design section of the new page and drag to the page the File Uploader element (You can be creative as you want here too ;) )
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(10).png?raw=true)
    Then go to the Workflow section -> Add an event -> Elements -> An input's value is changed
    Add an action -> Data -> Create a new thing -> Set the Type variable to PDFs and set another field as PDF = This FileUploader's value
    Add another action: Data -> Make changes to things and fill the fields as follow:
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(18).png?raw=true)
6- Convert PDF to Text:
    Install Convert PDF to Text plugin
    Got to workflow and add another action -> Plugins -> Convert PDF to Text, the pdf-url is going to be ThisFileUploader's value
    Add another action -> Data -> Make changes to a thing and you fill with the following
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(19).png?raw=true)
    This will add the PDF text to the content field of the PDF.
    When it comes to sending data to OpenAI API, you need to consider the number of tokens as it comes with a cost, to reduce the cost, you can summarize the PDF text
    Go ro Data -> PDFs -> Data Types -> Create a New field call it summary and the type is text
    Add another action -> Plugins -> OpenAI - GPT ( make sure that OpenAI and ChatGPT plugin is installed) and fill it as follow:
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(20).png?raw=true)
7- ChatGPT plugin
    Now you can intract with the PDF content, ask questions...
    But first let's clean up the UI, so that the user can upload as many PDFs. To do so, create another action -> Elements actions -> Reset inputs
    Another thing we want to add, is to show a message when the suer has successfully uploaded a PDF. To do so, go to Design section, drag the Browser plugin into the page (Make sure it is already installed) and go back to the Workflows section and add another section -> Element Actions -> Show alert Pop up in Browser and write the message you want.
    
    Now to feed all this knowledge base to openai, you add another action -> Plugins -> OpenAI - GPT (make sure that OpenAI and ChatGPT plugin is installed) and fill the fields as follow:
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(21).png?raw=true)

8- Display the result
    Now, to display the result in the page, to do so go to Design -> Add a Text element to the page -> Click Outside the page -> Click the i icon -> Create a new custom state, call it "result", and se type to text
    Click in the Text element -> and set in the appearance space: page_name's result 
    Go now to the Workflow section and add another action -> Element Actions -> Set State and replace the fiels as follow (Replace storepdfs with your actual page name)
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(22).png?raw=true)

you can be creative and add an input section to ask questions about the workbooks and get answer as well for the workbooks.
