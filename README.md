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


# Description

## `speller_app/views.py` Overview

The `views.py` file in the `speller_app` contains the logic for handling user requests and rendering responses. Below is a detailed explanation of the key views and their functionality:

### 1. `index(request)`
**Purpose**: Renders the homepage of the application.

- **Input**: 
  - `request`: HTTP request object.
- **Output**: Renders the `index.html` template, which serves as the landing page.

---

### 2. `spell(request)`
**Purpose**: Handles the main text correction functionality of the application.

- **Input**: 
  - `request`: HTTP request object with `POST` or `GET` data.
- **Logic**:
  - For `POST` requests:
    - Processes the user-submitted form (`TextInputForm`).
    - Uses the external `speller` function from `libs.text_handler` to generate a corrected version of the input text.
    - Stores the correction in the database for logged-in users (limits to 15 entries by replacing the oldest).
  - For `GET` requests:
    - Initializes an empty form for user input.
- **Output**: Renders the `speller.html` template with:
  - The original form.
  - The corrected text (if provided).
  - Dynamic background height adjustment for the corrected text area.
  
---

### 3. `report(request, report_id)`
**Purpose**: Displays a stored corrected text report from the database.

- **Input**: 
  - `request`: HTTP request object.
  - `report_id`: Primary key of the `Report` to retrieve.
- **Logic**:
  - Validates the user’s session.
  - Fetches the corresponding report text if the user is authenticated.
  - Redirects to the homepage if the user is not logged in.
- **Output**: Renders the `report.html` template with the stored corrected text.

---

### 4. `HistoryView(LoginRequiredMixin, ListView)`
**Purpose**: Provides a paginated view of a user’s correction history.

- **Inheritance**: 
  - Extends `ListView` for rendering object lists.
  - Uses `LoginRequiredMixin` to restrict access to logged-in users only.
- **Attributes**:
  - `template_name`: Points to the `history.html` template.
  - `context_object_name`: Names the context variable passed to the template.
- **Logic**:
  - Fetches and orders reports associated with the authenticated user by date (most recent first).
- **Output**: Renders the `history.html` template with a table of the user’s correction history.

---

## External Dependencies

- **`speller` Function**: 
  - Located in `libs.text_handler.src.methods`.
  - Processes user text and returns a corrected version.
- **Models**:
  - `User`: Django’s built-in user model.
  - `Report`: Custom model to store corrected text and metadata.

---

## Templates

The `views.py` functions interact with the following templates:
- `index.html`: Homepage template.
- `speller.html`: Displays the input form and corrected text.
- `report.html`: Shows a single stored correction.
- `history.html`: Displays a list of previous corrections.

This modular design ensures clear separation of concerns and ease of scalability for future features.


## `speller_app/models.py` Overview

The `models.py` file in the `speller_app` defines the database schema for storing corrected text reports. This file uses Django's ORM (Object-Relational Mapping) to interact with the database.

### 1. `Report` Model
The `Report` model represents a single corrected text entry associated with a user.

#### Fields:
- **`user`**: A `ForeignKey` linking each report to a specific user.
  - **Relation**: One-to-many (a user can have multiple reports).
  - **Cascade Delete**: If a user is deleted, all their associated reports are also removed.
  
- **`header`**: A `CharField` for storing a brief summary of the corrected text.
  - **Max Length**: 48 characters.
  - **Purpose**: Provides a quick overview of the correction (e.g., the first 46 characters followed by "...").

- **`text`**: A `TextField` for storing the full corrected text.
  - **Purpose**: Contains the entire corrected version of the user’s input.

- **`date`**: A `DateTimeField` for recording the timestamp of the report.
  - **Auto-Update**: Automatically updates to the current time whenever the report is modified.

#### Methods:
- **`__str__()`**:
  - Returns a string representation of the model instance.
  - Format: `Text(id[{self.pk}], header[{self.header}]); user(id[{self.user_id}])`.

---

### Example Usage
The `Report` model is used in:
- **`views.py`**:
  - To create, retrieve, update, and delete reports.
  - Ensures a maximum of 15 reports per user by replacing the oldest entry.
- **Templates**:
  - `history.html` displays a list of reports using the `header` and `date` fields.
  - `report.html` shows the full corrected text using the `text` field.

This model ensures efficient storage and management of user corrections in the database while maintaining flexibility for future enhancements.


## `users/views.py` Overview

The `views.py` file in the `users` application manages user-related functionalities such as registration, login, profile management, and password changes. Below is a breakdown of the provided views:

---

### 1. `registration(request)`
**Purpose**: Handles user registration.

- **Input**:
  - `request`: HTTP request object with `POST` data for form submission.
- **Logic**:
  - On `POST`:
    - Processes the submitted `UserRegistrationForm`.
    - Saves the new user if the form is valid.
    - Redirects to the login page upon success.
  - On `GET`:
    - Initializes an empty registration form.
- **Output**: Renders the `registration.html` template with the registration form.

---

### 2. `login(request)`
**Purpose**: Manages user authentication and login.

- **Input**:
  - `request`: HTTP request object with `POST` data containing username and password.
- **Logic**:
  - On `POST`:
    - Validates the `UserLoginForm`.
    - Authenticates the user using `auth.authenticate`.
    - Logs in the user and redirects to the application's homepage if authentication succeeds.
  - On `GET`:
    - Displays an empty login form.
- **Output**: Renders the `login.html` template with the login form.

---

### 3. `profile(request)`
**Purpose**: Allows users to view and update their profile.

- **Input**:
  - `request`: HTTP request object with `POST` data for profile updates.
- **Logic**:
  - Validates if the user is authenticated.
  - On `POST`:
    - Processes the `UserProfileForm` populated with the user’s data.
    - Saves changes if the form is valid.
  - On `GET`:
    - Displays the current user profile in an editable form.
  - Redirects to the login page if the user is not authenticated.
- **Output**: Renders the `profile.html` template with the profile form.

---

### 4. `logout(request)`
**Purpose**: Logs out the authenticated user.

- **Input**:
  - `request`: HTTP request object.
- **Logic**:
  - Calls `auth.logout` to end the user session.
  - Redirects to the application's homepage.
- **Output**: Redirects to the homepage.

---

### 5. `CustomPasswordChangeView`
**Purpose**: Provides functionality for authenticated users to change their passwords.

- **Inheritance**:
  - Extends `PasswordChangeView` to manage password changes.
  - Includes `LoginRequiredMixin` to restrict access to logged-in users.
- **Attributes**:
  - `template_name`: Specifies the `change_password.html` template.
  - `success_url`: Redirects to the user’s profile page upon successful password change.
  
---

## Templates

The `views.py` functions use the following templates:
- `registration.html`: Displays the user registration form.
- `login.html`: Displays the login form.
- `profile.html`: Shows and allows editing of the user’s profile.
- `change_password.html`: Provides a form for password changes.

These views are designed to ensure a seamless user experience, with secure authentication and intuitive navigation for account management tasks.


## `users/forms.py` Overview

The `forms.py` file in the `users` application defines forms for user-related functionalities, leveraging Django’s built-in forms framework. Below are the forms included:

---

### 1. `UserRegistrationForm`
**Purpose**: Handles new user registration.

- **Base Class**: `UserCreationForm`.
- **Customizations**:
  - Extends the default `UserCreationForm` to include additional fields if necessary.
  - Provides validation logic to ensure proper user data entry.
- **Fields**:
  - Includes fields like `username`, `password1`, `password2`, and other optional fields based on the project requirements.

---

### 2. `UserLoginForm`
**Purpose**: Manages user authentication during login.

- **Base Class**: `AuthenticationForm`.
- **Customizations**:
  - Simplifies the login process with validation for `username` and `password`.
- **Fields**:
  - Typically includes `username` and `password` inputs.

---

### 3. `UserProfileForm`
**Purpose**: Allows users to update their profile details.

- **Base Class**: `ModelForm`.
- **Customizations**:
  - Uses the `User` model to prepopulate and update user data.
  - Supports fields such as `first_name`, `last_name`, `email`, and other editable profile attributes.
- **Features**:
  - Ensures valid data entry and updates user information securely.

---

## Integration in Views
- **`UserRegistrationForm`**: Used in the `registration` view to register new users.
- **`UserLoginForm`**: Used in the `login` view to authenticate users.
- **`UserProfileForm`**: Used in the `profile` view to manage user updates.

This modular structure ensures clean, reusable, and maintainable code for user-related operations.
