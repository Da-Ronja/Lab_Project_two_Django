```markdown
# Lab 1

1. **Create your virtual environment**  
   Use this command as an example:
   ```bash
   conda create --name DjangoEnv python
   ```
   Activate the newly created environment and install Django:
   ```bash
   conda activate DjangoEnv
   pip install django
   ```

2. **Create a new Django project**
   - Name the project: `Project_two`

3. **Create a new Django app**
   - Name the app: `AppTwo`

4. **Create an Index View**
   - The view should return: `<em>My Second App</em>`

5. **Link the view to `urls.py`**
   - Ensure the Index View is accessible via a URL path.

---

# Lab 2 - Template Challenge

Continue with the `Project_two` project from Lab 1.

### Task:

1. **Create a templates directory**
   - Connect the templates directory to the `settings.py` file.

2. **Create a new view called `help`**
   - Use URL mapping to render this view for any page with the extension `/help`.

3. **Add template tags**
   - The `help` view template should include a tag that returns “Help Page”.

---

# Lab 3

Recreate the project we developed earlier, but with some modifications.

### Task:

1. **Create a Simple Profile Page**
   - The profile page should display a user’s profile photo and include a bio section beneath the photo.

2. **Use Bootstrap for Styling**
   - Use Bootstrap as the CSS framework for styling the profile page.

---

# Lab 4 
Recreate the project we worked on together in class.

### Task:
1. **Create and Register Models in Database**
   - Define and add models (Topic, Webpage, AccessRecord) to the project.
   - Register the models in the admin interface to enable management through Django's admin panel.

2. **Create a Data Populating Script**
   - Create a script to populate the database with dummy data using the Faker library.

3. **Integrate with Frontend**
   - Display the populated data on the website by connecting it to appropriate views and templates.
```