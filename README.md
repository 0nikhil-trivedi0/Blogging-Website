# Blogging-Website

A simple and interactive blogging platform built with Flask, Jinja, HTML, CSS, and Bootstrap.

## Features

- View all blog posts
- View individual blog posts
- Create new blog posts
- Responsive design with Bootstrap

## Project Structure

Blogging-Website/
├── app.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── post.html
│ ├── new_post.html
├── static/
│ ├── style.css
├── posts.json


## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/0nikhil-trivedi0/Blogging-Website.git
    cd Blogging-Website
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
4. **Run the Flask app:**
    ```bash
    python app.py
    ```

5. **Open the app in your browser:**
    Open `http://127.0.0.1:5000/` in your browser.

## Usage

- **Home Page:** Displays all blog posts with an option to read more.
- **Post Page:** Displays the full content of a blog post.
- **New Post Page:** Allows creating a new blog post.

## File Descriptions

- **app.py:** The main Flask application file.
- **templates/**: Contains HTML templates.
    - **base.html:** The base template with the navbar.
    - **index.html:** The home page template displaying all blog posts.
    - **post.html:** The template for displaying a single blog post.
    - **new_post.html:** The template for creating a new blog post.
- **static/**: Contains static files like CSS.
    - **style.css:** Custom CSS for additional styling.
- **posts.json:** JSON file to store blog posts data.

## Screenshots

### Home Page
![Home Page](https://github.com/0nikhil-trivedi0/Blogging-Website/screenshots/home_page.png)

### Post Page
![Post Page](https://github.com/0nikhil-trivedi0/Blogging-Website/screenshots/post_page.png)

### New Post Page
![New Post Page](https://github.com/0nikhil-trivedi0/Blogging-Website/screenshots/new_post_page.png)
