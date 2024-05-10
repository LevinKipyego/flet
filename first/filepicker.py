import flet as ft
from icecream import ic
import os 
import shutil

def main(page:ft.Page):
    def saveUploads(e: ft.FilePickerResultEvent):
        for file in e.files:
            ic(file.path)
            ic(file.name)
            
            copy_dir = os.path.join(os.getenv('USERPROFILE'), 'upload')
            
            ic(copy_dir)
            shutil.copy(file.path, copy_dir)
            page.update()
    
    file_picker =  ft.FilePicker(
        on_result=saveUploads
        
    )
    
    page.overlay.append(file_picker)
    page.theme_mode="light"
    upload = ft.ElevatedButton('Upload training data' , on_click= lambda e : file_picker.pick_files(allow_multiple=True))
    page.add(upload)

ft.app(target=main, upload_dir='upoad')