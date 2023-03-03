## Deployed using Python Anywhere

This project is hosted by Python Anywhere:
https://www.pythonanywhere.com/user/jakjarvis/

The current setup of the project in Python Anywhere is rather manual - no CI/CD (although this is apparently possible).

Small changes to files can be managed by deleting and reuploading the file in the Files tab, larger changes are usually handled by deleting the whole repo and recloning it using the Console.

After all changes, the site has to be reloaded using the button in the Web tab.

The deployment uses a virtual environment which must be activated in the console before installing any new pip dependencies.
workon jakjarvisvenv

The project is hosted at:
apps.jakjarvis.com
which is configured in Google Domains:
https://domains.google.com/registrar/jakjarvis.com/dns
