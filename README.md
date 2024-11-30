# Spella

Spella is a robust Django-based web application that assists users in correcting grammatical errors in their text. Designed with simplicity and functionality in mind, Spella caters to both anonymous and registered users by offering real-time grammar corrections and a unique history-tracking feature for logged-in users.

---

## Features

### 1. Real-Time Grammar Correction
Spella processes user-submitted text and identifies grammatical issues, delivering a corrected version instantly. It leverages advanced text analysis tools to ensure precise and meaningful corrections, enhancing the overall quality of written communication.

### 2. User Authentication and Registration
The application includes secure user authentication:
- **Account Creation**: Users can register to create a personalized account.
- **Login System**: Secure login with password encryption ensures user data privacy.
- **Session Management**: Spella efficiently handles user sessions for a seamless experience.

### 3. Submission History for Registered Users
Logged-in users gain access to a dynamic history feature:
- Tracks the last **15 submissions**.
- Displays corrections in reverse chronological order.
- Updates automatically as new submissions are made.
This feature enables users to reference their past inputs and corrections easily, making it ideal for learners and professionals refining their writing skills.

### 4. Database-Driven Backend
Spella employs a database to manage user accounts, submission histories, and corrections:
- **PostgreSQL** is used for local development.
- The application is compatible with **MySQL** for production environments.

### 5. Intuitive Interface
Spella's user interface is clean and straightforward, allowing users to focus on their tasks without unnecessary distractions:
- A single input field for text submission.
- A responsive design for usability across devices.
- Accessible features for both guests and registered users.

---

## Installation

To deploy Spella on your local machine, follow these steps:

### Step 1: Clone the Repository
Start by cloning the GitHub repository to your local machine:
```bash
git clone --recurse-submodules https://github.com/Koji255/spella.git
cd spella
```

### Step 2: Set Up the Environment
Ensure Python 3.8+ and pip are installed. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### Step 3: Install Dependencies
Install the required Python libraries listed in requirements.txt:
```bash
pip install -r requirements.txt
```

### Step 4: Configure the Database
Apply database migrations to set up the tables:
```bash
python manage.py migrate
```

### Step 5: Run the Development Server
Start the application by running:
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000 in your web browser to use Spella.

## Usage
### Anonymous Users
- Open the application in your browser.
- Enter text in the input field and submit.
- View the corrected text instantly on the results page.
### Registered Users
- Create an Acount
- Login
- Submission History
### Example Workflow
1. Visit the homepage.
2. Paste text (e.g., "I goes to the park yesterday.").
3. Submit the text and view the corrected version (e.g., "I went to the park yesterday.").
4. For registered users, revisit this correction in your history.

## Technologies Used
### Backend
- Django. A Python framework for rapid and secure web development.
- Django Template Language
- PostgreSQL. Free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance.
### Frontend
- HTML5. For structuring web content.
- CSS3. For styling and responsive design.
- JavaScript: For interactive and dynamic elements.
### Aditional Libraries
- My own 'text_handler' library for spell functionality.
- Django Authentication: Handles secure user login and registration.
- Database ORM: Simplifies data handling with Django's Object-Relational Mapping.

## Key Files and Directories
1. **`spella/settings.py`**: Contains configurations like installed apps, middleware, database settings, and static file configurations.
2. **`spella/urls.py`**: Central routing file connecting URLs to application-specific URLs.
3. **`app/models.py`**: Defines the data structure stored in the database, including user text submissions and history.
4. **`app/views.py`**: Implements the logic for handling user requests, processing text, and rendering templates.
5. **`app/templates/app/`**: Stores the HTML templates used for user-facing pages such as the homepage, login, and history view.
6. **`app/static/app/`**: Hosts static assets like CSS for styling and JavaScript for interactivity.
7. **`requirements.txt`**: Lists all Python dependencies needed for the project.

This modular organization ensures Spella is maintainable and can be extended with additional features in the future.

## Contributing
Spella welcomes contributions from the community. To get involved:
### Fork the Repository:
Click 'Fork' at the top of this page
### Clone the Fork:
```bash
git clone https://github.com/<your-username>/spella.git
```
### Create a Feature Branch
```bash
git checkout -b feature-name
```
### Commit Changes
### Submit a Pull Request
Explain your changes clearly and reference any related issues.
