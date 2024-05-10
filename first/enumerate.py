import flet as ft
from icecream import ic
import os 
import platform
import shutil

dir_input = ft.TextField(
                                 border_color=ft.colors.BLUE_200,
                                 focused_border_color=ft.colors.AMBER,
                                 hint_text='Enter the folder name you want to create',
                                 border='underline',
                                 filled=True,
                                 focused_color=ft.colors.AMBER,
                                 suffix_icon=ft.icons.FOLDER
                                 )
# Define global variables
current_os = platform.system()
path = None  # Initialize path variable globally

# Function to split uploaded files into training, testing, and validation folders
def split_folders(upload_dir):
    try:
        train_dir = os.path.join(os.getenv('USERPROFILE'), dir_input.value.strip(),  'training')
        os.makedirs(train_dir)
        test_dir = os.path.join(os.getenv('USERPROFILE'), dir_input.value.strip(), 'testing')
        os.makedirs(test_dir)
        validation_dir = os.path.join(os.getenv('USERPROFILE'), dir_input.value.strip(), 'validation')
        os.makedirs(validation_dir)
        
        # Here you can split the files into the respective folders
        # For example, move 70% of files to training, 20% to testing, and 10% to validation
        # You can customize this based on your requirements
        
        # Copy files to training folder
        # shutil.copy(source_file, train_dir)
        
        # Copy files to testing folder
        # shutil.copy(source_file, test_dir)
        
        # Copy files to validation folder
        # shutil.copy(source_file, validation_dir)
        
        ic('Folders split successfully!')
    except Exception as e:
        ic('An error occurred during folder splitting:', e)

def main(page:ft.Page):
    global path  # Access the global path variable
    page.theme_mode = 'light'
    page.padding=10
    
    def user_input():
        def pick(e):
           # nonlocal path  # Access the outer scope path variable
            
            if not dir_input.value:
                dir_input.error_text = 'directory name must not be empty' 
                page.update()
                return
            
            child = dir_input.value.strip()
            dir_input.value = ''
            page.update()
            
            new_dir = os.path.join(path, child)
            
            try:
                os.makedirs(new_dir)
                msg = ft.Text(f'Your Folder is created here: {new_dir}', size=17, color=ft.colors.AMBER_200, font_family='Poppins', weight='bold')
                page.add(msg)
            except FileExistsError as e:
                os_error = ft.Text(e)
                page.add(os_error)
                
            # Call function to split uploaded files into folders
            split_folders(new_dir)
                
            # File picker
            def save_uploads(e: ft.FilePickerResultEvent):
                #nonlocal path  # Access the outer scope path variable
                upload_dir = os.path.join(path, child)
                
                for file in e.files:
                    ic(file.path)
                    ic(file.name)
                    ic(upload_dir)
                    
                    shutil.copy(file.path, upload_dir)
                    page.update()
            
            file_picker =  ft.FilePicker(on_result=save_uploads)
            page.overlay.append(file_picker)
            page.add(ft.ElevatedButton('Upload training data', on_click=lambda e: file_picker.pick_files(allow_multiple=True)))
        
        page.add(dir_input, ft.ElevatedButton('create', on_click=pick))

    user_input()

ft.app(target=main, upload_dir= os.path.join(os.getenv('USERPROFILE'), dir_input.value.strip()))
