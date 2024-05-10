'''current_os = platform.system()'

def main(page):
    page.padding=10
    page.bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREY_100)
    
    def take_user_input():
        if current_os == "Android":
            external_storage  = os.getenv('EXTERNAL_STORAGE')
            child = ft.TextField(label='child directory')
    
        elif current_os == 'nt':
            external_storage  = os.getenv('USERPROFILE')
            child = ft.TextField(label='child directory')
                
        else:
            ic()
        
        def pick(e):
            if child.value == '':
                child.error_text='directory should not be empty'
                page.update()
                
                
                
            else:    
                child_dir = child.value
                child.value=''
                page.update()
                
                new_directory_path = os.path.join(external_storage, child_dir)
                try:
                    os.makedirs(new_directory_path,exist_ok=True)
                    msg = ft.Text(f'Your Folder is created hear: {new_directory_path}',size=17,color=ft.colors.AMBER_200,font_family='Poppins',weight='bold')
                    page.add(msg)
                    
                except OSError as e:
                    os_error=ft.Text(e)
                    page.add(os_error)
                    
                
        
        page.add(child, ft.ElevatedButton('create', on_click = lambda e : pick(e)))
        
        
    take_user_input()

ft.app(main)


def main(page):
    def make_dir(e):
        parent_directory = ft.TextField(label='parent dir')
        parent_directory=parent_directory.value
        ic(parent_directory)
        
        if not parent_directory:
            parent_directory = '/sdcard/' if os.name == 'poxis' else 'C:\\Users\\Public'
            
        else:
            parent_directory = parent_directory.strip()
            
        child_directory = ft.TextField(label='dir name')
        page.add(parent_directory,child_directory)
        
        new_directory_path = os.path.join(parent_directory, child_directory)
        
        try:
            os.makedirs(new_directory_path,exist_ok=True)
            msg = ft.Text(new_directory_path)
            page.add(msg)
            
        except OSError as e:
            txt=ft.Text(e)
            page.add(txt)
            
    btn=ft.ElevatedButton('make dir',on_click=make_dir)       
    page.add(btn)
ft.app(main)


import keyboard

def on_shortcut():
    print("Shortcut pressed!")

# Register a keyboard shortcut
keyboard.add_hotkey('ctrl+shift+a',on_shortcut)

try:
    # Keep the program running until interrupted
    keyboard.wait()
except KeyboardInterrupt:
    # Clean up when interrupted
    keyboard.remove_hotkey('ctrl+shift+a')


import flet as ft

def main(page: ft.Page):
    page.title = "Flet Chat"

    # subscribe to broadcast messages
    def on_message(msg):
        messages.controls.append(ft.Text(msg))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(f"{user.value}: {message.value}")
        # clean up the form
        message.value = ""
        page.update()

    messages = ft.Column()
    user = ft.TextField(hint_text="Your name", width=150)
    message = ft.TextField(hint_text="Your message...", expand=True)  # fill all the space
    send = ft.ElevatedButton("Send", on_click=send_click)
    page.add(messages, ft.Row(controls=[user, message, send]))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)

import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)


def main(page: Page):
    # Pick files dialog
    def pick_files_result(e: FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()

    # Save file dialog
    def save_file_result(e: FilePickerResultEvent):
        save_file_path.value = e.path if e.path else "Cancelled!"
        save_file_path.update()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()

    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Save file",
                    icon=icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web,
                ),
                save_file_path,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Open directory",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path,
            ]
        ),
    )


flet.app(target=main)


import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)


import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    page.on_route_change = route_change
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)

import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)



import flet as ft

def main(page: ft.Page):
    page.title = "Drag and Drop example 2"

    def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.src_id)
        # update text inside draggable control
        src.content.content.value = "0"
        # reset source group, so it cannot be dropped to a target anymore
        src.group = ""
        # update text inside drag target control
        e.control.content.content.value = "1"
        # reset border
        e.control.content.border = None
        page.update()

    def drag_will_accept(e):
        # black border when it's allowed to drop and red when it's not
        e.control.content.border = ft.border.all(
            2, ft.colors.BLACK45 if e.data == "true" else ft.colors.RED
        )
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=ft.Text("1"),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave,
                ),
            ]
        )
    )

ft.app(target=main)


import flet as ft
from icecream import ic

def main(page):
    def key_log(e: ft.KeyboardEvent):
        ic(e.key,e.shift, e.meta, e.control)
        
        
        
        
    page.on_keyboard_event = key_log
    
ft.app(target=main)    

def main(page: ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )
        
    
        with open('key_log.txt', "a") as f:
            
            if e.key:
                if e.key == 'Enter':
                    f.write('\n')
                f.write(e.key)
            
            f.close()    

    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys...")
    )

ft.app(target=main)



import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)

ft.app(target=main)



import flet as ft


def main(page):
    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

ft.app(target=main)













import flet as ft
from icecream import ic

def main(page):
    def say_hello(e):
        if not text_input.value:
            ic('hello')
            text_input.error_text = "input your name"
            page.update()
            
            
            
        else:
            name = text_input.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))   
        
    text_input=ft.TextField(label='Name')
    btn=ft.ElevatedButton('click me', on_click=lambda e:say_hello(e))
    
    page.add(text_input,btn)
ft.app(target=main)

'''