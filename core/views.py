from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import WefunderForm
from .models import Wefunder, WefunderImg, WefunderSqla
from pdf2image import convert_from_path

class Home(TemplateView):
    template_name = 'home.html'

# list all of companies's project
def core_list(request):
    forms = WefunderSqla.objects.raw("SELECT c.id, project_name, project_description, pdf_file, '/' || min( img_file ) img_file \
                                    FROM  core_wefunder c join core_wefunderimg i on c.id = pdf_id \
                                    group by c.id, project_name, pdf_file ")
    return render(request, 'core_list.html', {
        'forms': forms
    })

# create new project and convert pdf to images
def upload_core(request):
    if request.method == 'POST':
        form = WefunderForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save()
            # local path for convert to image
            convert_pdf_to_images( form1.pdf_file.path, form1.pdf_file.url, form1.pk)
            return redirect('core_list')
    else:
        form = WefunderForm()
    return render(request, 'upload_core.html', {'form': form})


def delete_core(request, pk):
    if request.method == 'POST':
        form1 = Wefunder.objects.get(pk=pk)
        form1.delete()
        formImg = WefunderImg.objects.filter(pdf_id=pk)
        for item in formImg:
            item.delete()
    return redirect('core_list')

def core_detail( request, pk):
     form1 = Wefunder.objects.get(pk=pk)
     formImg = WefunderImg.objects.filter(pdf_id=pk)
     return render(request, 'core_detail.html', {'form': form1, 'formImg': formImg})

# covert pdf to images and save to file system and save path to database
#  argument must be a relative path, not an absolute path.
def convert_pdf_to_images(pdf_path,web_path, pid):
    images = convert_from_path(pdf_path)
    file_name = convert_file_name( pdf_path, pid )
    img_name = convert_file_name( web_path, pid )

    for index, image in enumerate(images):
        img_file_name = f'{file_name}-{index}.png'
        web_img_name = f'{img_name}-{index}.png'
        image.save(img_file_name)
        WefunderImg.objects.create(pdf_id=pid, img_file=web_img_name[1:])

# convert image name with pid
def convert_file_name( file_path, pid ):
    path_list = file_path.split('/')
    path_list[-1] = str(pid)
    return "/".join(path_list)








