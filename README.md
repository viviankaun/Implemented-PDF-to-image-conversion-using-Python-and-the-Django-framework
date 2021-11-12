# upload pdf then convert to images :
Upload pdf to the system and it will automatically split into multiple images.
When we delete our data aslo remove the files on our file system. 
 

## SQLlite with model :
1. Create a model for multiple tables 
'''
Model.objects.raw("SELECT c.id, project_name, project_description, pdf_file, '/' || min( img_file ) img_file \
                                    FROM  core_wefunder c join core_wefunderimg i on c.id = pdf_id \
                                    group by c.id, project_name, pdf_file ")
'''
                                    
2. Merge coloumns using || syntax which it is differnet MSSQL, MYSQL    


##Table:
![This is an image](https://github.com/viviankaun/Project-Python-django/blob/main/img/table01.jpg)
Django Model : Each Model has default PRIMARY KEY with auto increment.
 

#
- Django==2.1.3
- python==3
- django-crispy-forms==1.7.2
- pytz==2018.4
- pdf2image 
                             
       
       
