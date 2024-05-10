import flet as ft
from icecream import ic
import os 
import platform
import shutil

current_os = platform.system()

dir_input = ft.TextField(
                                 border_color=ft.colors.BLUE_200,
                                 focused_border_color=ft.colors.AMBER,
                                 hint_text='Enter the folder name you want to create',
                                 border='underline',
                                 filled=True,
                                 focused_color=ft.colors.AMBER,
                                 suffix_icon=ft.icons.FOLDER
                                 )
    




def main(page:ft.Page):
    page.theme_mode = 'light'
    page.padding=10
    
    
    
    
    def user_input():
        
        
        def pick(e):
            if os.name == 'posix':
                path = os.getenv('ANDROID_STORAGE')
                
            elif current_os == 'Windows':
                path = os.getenv('USERPROFILE')
                
            elif current_os in ['Darwin', 'Linux']:
                path = os.getenv('HOME')
                
            else:
                ic('invalid os') 
                
            if not dir_input.value:
                dir_input.error_text = 'directory name must not be empty' 
                page.update()
            
            else:
                child = dir_input.value.strip()
                dir_input.value = ''
                page.update()
            
            new_dir = os.path.join(path, child)
            
            try:
                os.makedirs(new_dir)
                
                
                msg = ft.Text(f'Your Folder is created hear: {new_dir}',size=17,color=ft.colors.AMBER_200,font_family='Poppins',weight='bold')
                page.add(msg)
            
            except FileExistsError as e:
                os_error=ft.Text(e)
                page.add(os_error)
                
             #File picker
            def saveUploads(e: ft.FilePickerResultEvent):
                for file in e.files:
                    ic(file.path)
                    ic(file.name)
                    
                    upload_dir = os.path.join(path,child)
                    ic(upload_dir)
                    
                    shutil.copy(file.path, upload_dir)
                    page.update()
            
            file_picker =  ft.FilePicker(
                        on_result=saveUploads
                        
                    )
                    
            page.overlay.append(file_picker)
                    
                    
                
            page.add(ft.ElevatedButton('Upload training data' , on_click= lambda e : file_picker.pick_files(allow_multiple=True)))

        
        
        page.add(dir_input, ft.ElevatedButton('create', on_click = lambda e : pick(e)),)
    
    user_input()
    
   
ft.app(target=main, upload_dir='upload')


