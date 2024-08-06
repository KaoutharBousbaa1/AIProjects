# Workbooks AI Application

Bubble is a full-stack, no-code app builder. You can build scalable applications with this AI-powered no-code development platform. You can also connect your app with ChatGPT or Claude. If you love reading like I do, you may come across countless workbooks. To make sure you ace them, you can stay organized and have them all in one place. Bubble can help you with that by gathering the workbooks listed in your favorite book in one place. This application is powered by the OpenAI API, and everything is done via the UI. Here are the steps to make one for you:

### Step 1: Set the API Connector

1. Install the API Connector
   
![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(2).png?raw=true)
   
2- Connect it to OpenAI by filling in the headers as follows:

![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(3).png?raw=true)
    
Make sure to replace `Bearer "YOUR_OPENAI_KEY_KEY"` with your actual OpenAI key. In this particular project, we used one API call, and that is to the Chat Completions Model. It is a POST request, and we are making a POST request to the following URL:         
`https://api.openai.com/v1/chat/completions`. You can change the `max_tokens` variable to make the application more scalable.

![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(4).png?raw=true)
    
Then click on Reinitialize Call and make sure that the messade_content's type is text.
    
3- Create a new data type:
To store the files that are related to each user, you need to create a new data type.
Navigate through the Data Types and create a new data type called PDFs.

    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(11).png?raw=true)
    
In the PDFs data type, create the following fields: `PDF` of type `file`, `content` of type `text`, `Full name` of type `text`
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
    ![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/WorkbookAI/Screenshot%20(18).png?raw=true
    
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

You can be creative and add an input section to ask questions about the workbooks and get answer as well for the workbooks.

# Travel AI Application
This project involves building an AI travel agent that helps you plan your travels based on your preferences.

## Make: Automation Software
Make is a no-code platform that allows you to visualize, create, build, and automate workflows.
This Make scenario is designed to generate a custom travel plan based on a user's interests and then store the generated plan in a Notion database. It connects to OpenAI's GPT-3 and Notion to achieve this. The Basic Repeater ensures the actions are repeated a specified number of times, the OpenAI GPT-3 module generates the travel plan, and the Notion module stores the plan in a database.
![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/TravelBot/Screenshot%20(7).png?raw=true)

#### Basic Repeater (Module ID: 8)
This module repeats a set of actions a specified number of times. It will repeat the subsequent actions three times, starting from 1 and incrementing by 1 each time.
* Configuration:
    - Start: 1
    - Repeats: 3
    - Step: 1

#### Transform Text to Structured Data (OpenAI GPT-3) (Module ID: 1)
This module uses OpenAI's GPT-3 to transform a text prompt into structured data. It generates a custom travel plan based on the user's interests in specific anime and outputs structured data.
* Configuration:
    - Model: gpt-4o
    - Prompt: "You are a personal travel agent with the goal of designing a custom travel plan from west coast Vancouver to the east coast North America. I’ve been really into anime like Frieren, kino's journey, and Somali and the forest spirit so I’d like to replicate some of their travels but on earth. Suggest a detailed plan for me. Eg: Title, date, location, nearest city/country, description, number of hours, category, weather."
    - Raw Text: {{executionId}}
    - Parameters:
        - Title (Type -> Title)
        - Date (Type -> Text)
        - Location (Type -> Text)
        - City (Type -> Text)
        - Description (Type -> Text)
        - Hours (Type -> Number)
        - Category (Type -> Text)
        - Weather (Type -> Text)
          
    Make sure to use a valid OpenAI Key.
  
#### Create a Page (Notion) (Module ID: 2)
This module creates a new page in a specified Notion database using the structured data generated by the previous module. It creates a new page in the specified Notion database with the travel plan details.
* Configuration:
    - Database ID: "your_data_base_id"
    - Fields Mapping:
        - Title: `{{1.Title}}`
        - Category: `{{1.Category}}`
        - Location: `{{1.Location}}`
        - Hours: `{{1.Hours}}`
        -Description: `{{1.Description}}`
        - Date: `{{1.Date}}`
        - Weather: `{{1.Weather}}`
        - City: `{{1.City}}`
    Make sure you create a database in notion with the same columns names and data types.
    To find the database ID, navigate to the Notion page where your database is locate, then Click on the database to open it, look at the URL in your browser's address bar. It will look something like this:
    `https://www.notion.so/yourworkspace/Database-Name-6feda45bc86e424488b4e534f63ee923`
    The Database ID is the long string of characters after the last slash (/) in the URL. In the example above, the Database ID is:
    `6feda45bc86e424488b4e534f63ee923`.
![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/TravelBot/Screenshot%20(8).png?raw=true)

## Streamlit Dashboard
This part of the project will send an api requestopn to openai's model to geerate travel suggestion and then it saved as a csv file itinerary_events.csv, and then it generates a streamtit dashboard, and the pyhton script generates also a google map with located areas that the ai suggested earlier. To run the project:
![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/TravelBot/Screenshot%20(10).png?raw=true)
![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/TravelBot/Screenshot%20(6).png?raw=true)
* Open the termianl and navigate to the folder
* run the following coommands:
    ```sh
    pip install --upgrade pip
    ```
    ```sh
    pip install -r requirements.txt
    ```
* Open steamlit.ipynb and run it in your IDE. 
* Run in the terlinal the following scripts: 
    ```sh
    python generate_coordinates.py
    ```
    ```sh
    streamlit run streamlit_app.py
    ```
Make sure to use a valid OpenAI key, and make sure to enable the Geocoding API in your Google Cloud Account, and to use a valid API key.

# AI Music Generator
The project involves creating music playlists using AI tools. It starts with generating multiple songs on the Udio platform. A script is written to connect the individual songs into a cohesive playlist, which is outputted in MP3 format. Text lyrics, potentially obtained through Whisper-1, are then transformed into prompts that encapsulate the imagery, mood, and vibes of the songs. These prompts are fed into DALL·E to generate corresponding images. Finally, the project combines the playlist with the generated images to create an MP4 file, resulting in a visually beautiful music experience.
To run the project:
* Generate AI music via Udio platform. You can sign up [here](https://www.udio.com/)
* Open the termianl and navigate to the folder
* run the following coommands:
    ```sh
    playlist.py
    ```
    ```sh
    python playlist_images.py
    ```
Make sure to use a valid OpenAI key.
# Personal Finance Chatbot:
This project aims to create a personal finance chatbot that helps you understand you spending habits and achieve financial goals. The chatbot, designed with the positive and perceptive personality of Might Guy from Naruto, uses GPT4All for prompt engineering and operates locally to ensure privacy. Users can interact with the chatbot using their CSV financial statements to analyze current spending habits. The project involves enhancing the chatbot's capabilities with Ollama in a Jupyter Notebook to categorize transactions and generate visualizations using a Plotly dashboard. 
![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/FinancialChatbot/Screenshot%20(1).png?raw=true)
Advanced features include integrating Retrieval-Augmented Generation (RAG) with LangChain and Flask, allowing the chatbot to provide more accurate and reliable financial advice through a lightweight web application. This comprehensive approach combines local execution, data privacy, and advanced AI techniques to offer insightful and actionable financial guidance.
To run the project:
* Download and install Ollama [here](https://ollama.ai/)
* Open the terminal and run the following commands:
    ```sh
    pip install --upgrade pip
    ```
    ```sh
    pip install -r requirements.txt
    ```
* Run the jupyternotbook in youe IDE: categorize_expenses.ipynb to categorize youe expenses
* Run the jupyternotbook in youe IDE: dashboard.ipynb to generate the dashboard
* Run the application by using the command:
    ```sh
    python chatbot.py
    ```
Make sure to use a valid OpenAI key and a valid Huggingface API key.
