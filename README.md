# Zeotap_chatbot
Chatbot with scraper

**Screenshot of UI**

<img width="945" alt="Screenshot 2025-02-28 200810" src="https://github.com/user-attachments/assets/4e05fe77-a8c8-4d53-af65-5964f41ab3e0" />

**Example of response -**

Question: What APIs does mparticle?

Response - mParticle provides several SDKs and APIs allowing you to collect data from a variety of sources, like a mobile app, web app, or data feeds from other SaaS providers

Question: How can I create a user profile in mParticle?

Response - On the Information tab for the profile, scroll to the User Attributes section and click theEditpencil icon next to the mParticle workspace where you want to make your changes https://docs.mparticle.com/guides/platform-guide/activity/#user-activity: For details, refer to the documentation for your integrations or contact your mParticle account representative.Edit a profileâs user attributesTo edit a profileâs user attributes:Navigate toActivity > User Activityusing the left-hand nav bar.Find the profile you want to edit by searching for one of the profileâs identifiers under User Search.On the Information tab for the profile, scroll to the User Attributes section and click theEditpencil icon next to the mParticle workspace where you want to make your changes.Remember that user attributes are scoped at the workspace level, so a profile that exists in multiple workspaces may contain different attributes in each workspace.In the Edit modal, select one of your configured and active inputs



This is a Retrieval-Augmented Generation (RAG) chatbot designed to assist users with CDP (Customer Data Platform) support queries. The chatbot scrapes documentation, stores the data in a vector database, and retrieves relevant answers using NLP-based approaches.

**Features**

Chatbot UI

Web Scraper to extract data from CDP documentation

Vector Database for efficient retrieval

NLP-based Answering System

**Tech Stack**

**Backend:**
 1. Python (Flask/FastAPI)
 2. LangChain for retrieval
 3. FAISS( vector DB)
 4. BeautifulSoup (Web Scraper)
 5. HuggingFace Transformers (NLP)

**Frontend:**

 1. React.js
 2. Tailwind CSS / Material UI
 3. Axios (for API calls

**Backend Setup**
cd backend  # Navigate to backend folder
python -m venv venv  # Create a virtual environment

**Activate virtual environment**
For Linux/macOS
source venv/bin/activate  
**For Windows**
venv\Scripts\activate  

pip install -r requirements.txt  # Install dependencies

**Backend Start**
python app.py  # For Flask
uvicorn main:app --reload  # For FastAPI

**Frontend Setup**
cd frontend  # Navigate to frontend folder
npm install  # Install dependencies
npm start  # Run React frontend


 
