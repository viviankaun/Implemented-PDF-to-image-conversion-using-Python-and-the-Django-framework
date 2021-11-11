# upload pdf then convert to images :
 

 

# SQLlite with model :
1. Create a model for multiple tables 
Model.objects.raw("SELECT c.id, project_name, project_description, pdf_file, '/' || min( img_file ) img_file \
                                    FROM  core_wefunder c join core_wefunderimg i on c.id = pdf_id \
                                    group by c.id, project_name, pdf_file ")
                                    
2. Merge coloumns using || syntax which it is differnet MSSQL, MYSQL    


# django Framework:
When we delete our data aslo delete the files on our file system. 



#Table:
![This is an image](https://github.com/viviankaun/Project-Python-django/blob/main/img/table01.jpg)

# for convert to images  
pdf2image 
                             
       
       
