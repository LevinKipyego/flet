import flet as ft
from icecream import ic

def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        ic(selected_files.value )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        )
    )

ft.app(target=main)


'''import os
import platform
from icecream import ic

def create_directory():
    # Get the current operating system
    current_os = platform.system()

    if current_os == 'Android':
        # For Android, use the external storage directory
        external_storage = os.getenv('EXTERNAL_STORAGE')
        if external_storage:
            directory_name = input('Enter directory name: ')
            new_directory = os.path.join(external_storage, directory_name)
            try:
                os.makedirs(new_directory)
                print(f'Directory {directory_name} created successfully!')
            except OSError as e:
                print(f'Failed to create directory: {e}')
        else:
            print('External storage not found on Android device.')
    elif current_os == 'Windows':
        # For Windows, use the user's home directory
        home_directory = os.getenv('USERNAME')
        ic(home_directory)
        if home_directory:
            directory_name = input('Enter directory name: ')
            new_directory = os.path.join(home_directory, directory_name)
            try:
                os.makedirs(new_directory)
                print(f'Directory {directory_name} created successfully!')
            except OSError as e:
                print(f'Failed to create directory: {e}')
        else:
            print('Home directory not found on Windows system.')
    elif current_os in ['Darwin', 'Linux']:
        # For macOS and Linux, use the user's home directory
        home_directory = os.getenv('HOME')
        if home_directory:
            directory_name = input('Enter directory name: ')
            new_directory = os.path.join(home_directory, directory_name)
            try:
                os.makedirs(new_directory)
                print(f'Directory {directory_name} created successfully!')
            except OSError as e:
                print(f'Failed to create directory: {e}')
        else:
            print('Home directory not found on macOS or Linux system.')
    else:
        print(f'Unsupported operating system: {current_os}')

if __name__ == '__main__':
    create_directory()


import os
import subprocess

def open_file_manager(path):
    # Determine the appropriate command based on the operating system
    if os.name == 'nt':  # Windows
        command = ['explorer', path]
    elif os.name == 'posix':  # macOS or Linux
        command = ['open', path]
    else:
        raise NotImplementedError("Unsupported operating system")
    
    # Open the file manager at the specified directory
    subprocess.run(command)

# Example usage:
directory_path = 'C:\\Users\\Public\\data'
open_file_manager(directory_path)
'''