# Employee-Records
This is a django based Web App for keeping records of Employees of a company.  
You can Keep records like Employee Id, Name, Surname, Job Title, Email and Address.

# Instructions to Deploy this Web App on Python Anywhere

* Create an Account on [Python Anywhere](https://www.pythonanywhere.com/) and login.
* Click on Bash in Consoles tab.
* In the bash terminal use this commands.

```bash
  mkvirtualenv --python==3.7.7 <virtualenv_name>
  pip install -U django
  git clone https://github.com/Shivam-Pancholi/Employee-Records.git
  cd EmployeeList
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  Fill out the fields to create super user.
 ```
 
## Setting up the Web App Domain Name
* Click on Dashboard in upper-right corner of the page.
* Go to Web tab.
* CLick on Add a new web app.

Here you will see a default domain name for this app but if you want to use your own domain name than follow this steps.
[Setting up the Custome Domain Name](https://help.pythonanywhere.com/pages/CustomDomains/)

* If you dont have your custome doamin name use the default domain name which is visible to you.
* Click on next.
* Select Django as python web framework in the list.
* Selct manual configuration.
* Select python version 3.7.
* Select Next.
* Now in Web tab scroll to Virtualenvs section.
* Write path to virtualenv i.e. /home/<your_username>/.virtualenvs/<virtualenv_name>/ and click Check.
* Scroll down to Static files section.
If you don't add this static files url and directory path your admin page will not look like before it will be loaded in basic html formet.
* Add URL as /static/admin.
* Add Directory as /home/<your_username>/.virtualenv/<virtualenv_name>/lib/python3.7/site-packages/django/contrib/admin/static/admin.
* Scroll up to Code section.
* Write path to the source code i.e. /home/<your_username>/Employee-Records/ and click Check.
* Now click on link to WSGI configuration file.
* End type bellow available code. Note :- Make sure a lot of code is already availbale in this file in commented for you just have to uncomment those.

```Py
  import os
  import sys
  import django
  from django.core.wsgi import get_wsgi_application

  path = '/home/<your_user_name>/Employee-Records'
  if path not in sys.path:
      sys.path.append(path)

  os.chdir(path)
  os.environ.setdefault("DJANGO_SETTINGS_MODULE","Employee-Records/Company.settings")

  django.setup()

  application = get_wsgi_application()
```
* Click Save on upper right corner.

Now open Files tab in home page.
* Click on Employee-Records -> Company -> settings.py.
* Scroll in settings.py file to Allowed Hosts list.
* Add Your domain name in allowed host like that :- ```ALLOWED_HOSTS = ['Domain-Name.com',]```
* Set Debug = False
Now go open Web tab reload your domain link.
* Now bowse your Domain, your website is deployed.

## How to use this app.

### Steps to Login.

* Create a User Account by Sign Up.  
* Fill all required fields.  
* Click Register.  
* Click Sign In.  
* Enter username and Password.  
* Click Log In.  

### Steps to Add a new Employee.

* Click on Add Employee to add a new employee.  
* Fill out the details.  
* Click save.  

### Steps to Update or Edit deatils of an Employee.

* Click on name of the employee.  
* Click on Edit button.  
* Edit the desired fields.  
* Click save.  

### Steps to Delete an Employee Record.

* Click on name of the employee.  
* Click on Delete button.  
* Click confirm.  
