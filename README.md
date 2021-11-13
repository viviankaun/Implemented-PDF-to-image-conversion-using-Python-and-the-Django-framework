# Upload pdf then split to images :
Upload pdf to the system and it will automatically split into multiple images.
When we delete our data aslo remove the files on our file system. 
 
###
urls.py : URL configuration.  
view.py : Most of the logic flow.
model.py: Generally, each model maps to a single database table.
form.py : we use customized form and map to table.


## SQLlite with model :
1. Create a model for multiple tables 
```
Model.objects.raw("SELECT c.id, project_name, project_description, pdf_file, '/' || min( img_file ) img_file \
                                    FROM  core_wefunder c join core_wefunderimg i on c.id = pdf_id \
                                    group by c.id, project_name, pdf_file ")
```                                    
2. Merge coloumns using || syntax which it is differnet MSSQL, MYSQL    
3. login SQLlite
```
(.env) > python manage.py dbshell
sqlite > .table
```


##Table:
![This is an image](https://github.com/viviankaun/Project-Python-django/blob/main/img/table01.jpg)
Django Model : Each Model has default PRIMARY KEY with auto increment.
 
## preparre environment
```
python3 -m venv .eenv 
source .env/bin/activate
pip install django
django-admin startproject mysite
python manage.py startapp core
```
## when we modifie model
```
python manage.py makemigrations
python manage.py migrate
```

### requirements
- Django==2.1.3
- python==3
- django-crispy-forms==1.7.2
- pytz==2018.4
- pdf2image 
                             
       
       
