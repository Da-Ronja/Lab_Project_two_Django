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
```