from flet import *
from test  import list 
def main(page: Page):
    page.padding=0
    
        
        
    bg = '#041955'
    width = 400
    height = 850
    fg = '#3450a1'
    fwg = '#97b4ff'
    pink = "#eb06ff"
    

    
    def shrink(e):
        page_2.controls[0].width=120
        page_2.controls[0].scale=transform.Scale(
            0.8,alignment=alignment.center_right
        )
        page_2.controls[0].padding=20
        page_2.controls[0].border_radius=border_radius.only(
            top_left=20,
            bottom_left=20,
        )
        page_2.update()
        
    def restore(e):
        page_2.controls[0].width=400
        page_2.controls[0].scale=transform.Scale(
            1,alignment=alignment.center_right
        )
        page_2.update()    
    
    categories_card=Row(scroll='auto')
    categories=['Family','Business','Friends'
                ]
    
    tasks=Column(height=300,
                 scroll='auto')
    
    for i in range(15):
        tasks.controls.append(
            Container(width=300,height=40,bgcolor=bg,
                      border_radius=10,
                      )
        )
        
    
    for index ,category in enumerate(categories):
        categories_card.controls.append(Container(
            height=110,width=170,
            bgcolor=bg,
            border_radius=20,
            padding=15,
            content=Column(
                controls=[
                Text('40 Tasks'),
                Text('Category'),
                Container(width=170,
                          height=5,
                          bgcolor='white',
                          border_radius=2,
                          padding=padding.only(right=index*30,),
                          content=Container(bgcolor=pink,),
                          ),
                          
            ]
            )
        ))
    add=Row(scroll='auto',)
    for i in list:
        add.controls.append(
            Container(
                content=Row(
                    controls=[
                        Container(width=120,
                                      border_radius=20,
                                      padding=20,
                                      height=70,
                                      bgcolor='white',
                                      content=Column(
                                          controls=[
                                              Text(i['task']),
                                              Text(i['category'])
                                          ]
                                      ))
                    ]
                )
                
            )
        )  
        
         
    create_task_view =Container(
        width=400,
        height=850,
        bgcolor=bg,
        padding=padding.only(top=60,right=50,left=50,),
        border_radius=30,
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                         on_click=lambda _: page.go('/'),
                         height=40,
                         width=40,
                         content=Icon(icons.CLOSE_OUTLINED)),
                    ]
                        ),
                add,
            ]
        )
        
    )
    
    
        
    first_page_content = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spacebetween',
                    controls=[
                        Container(
                            on_click=lambda e : shrink(e),
                            content=Icon(
                                icons.MENU
                            )),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED),
                            ] )
                    ] ),
                Container(height=20),
                Text(value='What\'s up June'),
                Text(value='CATEGORIES'),
                Container(padding=padding.only(top=10,bottom=20),
                          content=categories_card),
                
                Text(value="TODAY'S TASK"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            icons.ADD,on_click = lambda _: page.go('/create_task'),
                            bottom=0,right=2,
                            bgcolor=pink,
                            width=40,
                            height=40,
                            
                            ),
                    ]
                ),
                
            ]
        )
    )
    page_1 = Container(
        width=400,
        height=850,
        bgcolor=bg,
        border_radius=30,
        padding = padding.only(
                    top=60,left=50,
                    right=140
                ),
        content=Column(
            controls=[
               Row(alignment='end',
                    controls=[
                    Container(
                    on_click=lambda e : restore(e),
                    border_radius=10,
                    height=25,width=25,border=border.all(color='white',width=2),
                    content=Icon(icons.CLOSE_FULLSCREEN,size=15)
                )
                ]),
                Container(height=20),
                Container(width=90,
                  height=90,
                  border_radius=45,
                  bgcolor='white',
                  ),
                Text('June',size=20,weight='bold',height=25),
                Text('Kimberley',size=20,weight='bold'),
                Container(height=20),
                Row(
                    controls=[
                        Icon(icons.FAVORITE_BORDER_SHARP,size=14,color='white',),
                        Text('Favorite Tasks',font_family='Poppins',size=14,weight=FontWeight.W_300),
                    ]
                ),
                Row(
                    controls=[
                        Icon(icons.SETTINGS_ACCESSIBILITY),
                        Text('Service',font_family='Poppins',size=14,weight=FontWeight.W_200)
                    ]
                ),
                Row(
                    controls=[
                        Icon(icons.SETTINGS_ACCESSIBILITY),
                        Text('Service',font_family='Poppins',size=14,weight=FontWeight.W_200)
                    ]
                ),
                
                Row(
                    controls=[
                        Icon(icons.SETTINGS_ACCESSIBILITY),
                        Text('Service' ,font_family='Poppins',size=14,weight=FontWeight.W_200)
                    ]
                ),
            ]
        )
    )
    
    page_2 = Row(alignment='end',
        controls=[
            Container(
                
                width=400,
                height=850,
                bgcolor=fg,
                border_radius=30,
                animate=animation.Animation(600,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400,curve='decelerate'),
                padding = padding.only(
                    top=50,left=20,
                    right=20,bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_content
                    ]
                )
            )
        ]
    )
    
    container = Container(
        width=width ,
        height=height, 
        bgcolor=bg,
        border_radius=30,
        
        content= Stack(
            controls=[
                page_1,
                page_2
            ]
        )
        
        )
    
    pages = {
        '/':View(
            "/",
            [
                container
            ],),
        '/create_task':View(
            "/create_task",
            [
                create_task_view
                ]
            ,),
    }
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
            )
        
    page.add(container)
    
            
    page.on_route_change = route_change
    page.go(page.route)
    

app(target=main)