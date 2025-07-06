import os
import sys
import img2pdf
import glob
from natsort import os_sorted

def ImgforPDF(img_path):
    fse = sys.getfilesystemencoding()

    pdf_path = os.path.join(img_path,'pdf_files_I2P')
    print(pdf_path + '\n')
    if pdf_path not in glob.glob(os.path.join(img_path,'*')):
        try: 
            os.mkdir(pdf_path)
        except:
            print('The directory is invalid! \nRestart the program and try again.')

    manga_path = os_sorted(glob.glob(os.path.join(img_path,'*')))
    for folder in manga_path:
        check = False
        if pdf_path in folder:
            continue

        name = folder.split('\\')[-1]
        pdf_name = os.path.join(pdf_path, name + '.pdf')
        new_name = name.replace('[','(')
        new_name = new_name.replace(']',')')
        if new_name != name:
            name = new_name
            new_path = os.path.join('\\'.join(folder.split('\\')[:-1]), name)
            os.rename(folder, new_path)
            folder = new_path
            pdf_name = os.path.join(pdf_path, name + '.pdf')
        
        if pdf_name in glob.glob(os.path.join(pdf_path,'*')):
            check = True
            continue

        images = []
        img_dir = os.path.join(folder,'*')
        print(name)
        img_files = os_sorted(glob.glob(u'{}'.format(img_dir)))
        for img_file in img_files:
            if img_file.endswith(('.jpg', '.JPG', '.jpeg', '.png', '.PNG', '.gif', '.webp')):
                images.append(img_file)
            else:
                print (img_file +' Unable to convert this file')
      
        if check == True:
            continue
        if images:
            try:
                pdf_data = img2pdf.convert(images) 
                with open(pdf_name, "wb") as file:
                    file.write(pdf_data) 
            except:
                print ('Unable to convert images ('+pdf_name+') due to one or more images have problem')  
    return   

manga_path = input('Enter the Directory: ')
ImgforPDF(manga_path)
input('Complete \nPress enter to close')
