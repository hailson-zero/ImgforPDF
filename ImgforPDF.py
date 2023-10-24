import os
import sys
import img2pdf
import glob

def ImgforPDF(img_path):
    fse = sys.getfilesystemencoding()

    pdf_path = os.path.join(img_path,'pdf_files')
    print(pdf_path + '\n')
    if pdf_path not in glob.glob(os.path.join(img_path,'*')):
        os.mkdir(pdf_path)

    manga_path = sorted(glob.glob(os.path.join(img_path,'*')), key=len)
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
        img_files = sorted(glob.glob(u'{}'.format(img_dir)), key=len)
        for img_file in img_files:
            if img_file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                images.append(img_file)
            else:
                print (img_file +' Unable to convert this file')
                    
        if check == True:
            continue
        if images:
            pdf_data = img2pdf.convert(images)
            with open(pdf_name, "wb") as file:
                file.write(pdf_data)
    return   

manga_path = input('Enter the Directory: ')
ImgforPDF(manga_path)
input('Complete\nPress enter to close')