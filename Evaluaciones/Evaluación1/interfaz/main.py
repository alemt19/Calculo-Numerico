import flet as ft
import numpy as np


def main(page: ft.Page):
    page.window_height = 395
    page.window_width = 700
    
    sizeCont = ft.TextField(
        value="3",
        read_only=True, 
        expand=1,
        border_radius=10
        )

    def minus_click(e):
        sizeCont.value = str(int(sizeCont.value) - 1)
        page.update() 
    
    def plus_click(e):
        sizeCont.value = str(int(sizeCont.value) + 1)
        r[0].height += 103
        r[0].width += 150
        t.tabs[1].content.content.controls[0].controls[0].columns.append(ft.DataColumn(ft.Text("x" + sizeCont.value), numeric=True))
        r[0].rows.append(ft.DataRow(cells=[]))
        for i in range(0, int(sizeCont.value)):
            r[0].rows[i].cells.append(ft.DataCell(ft.TextField("0", border_width=0)))

        page.update()
    
    def erase_click(e):
        resultText.value = " "
        for i in range(0, int(sizeCont.value)):
            t.tabs[1].content.content.controls[0].controls[1].rows[i].cells[0].content.value = "0"
            for j in range(0, int(sizeCont.value)):
                t.tabs[1].content.content.controls[0].controls[0].rows[i].cells[j].content.value = "0"
        page.update() 
    
    def calc_click(e):
        a = []
        b = []
        for i in range(0, int(sizeCont.value)):
            b.append(int(r[1].rows[i].cells[0].content.value))
            row = []
            for j in range(0, int(sizeCont.value)):
                row.append(int(r[0].rows[i].cells[j].content.value))
            a.append(row)
        resultado = gJordan(np.array(a), np.array(b))
        if str(type(resultado)) == "<class 'str'>":
            resultText.value = resultado
        else:
            resultText.value = str(resultado)
        page.update()

    plusButton = ft.ElevatedButton(
        text="+",
        bgcolor=ft.colors.BLUE_GREY_100,
        color=ft.colors.BLACK,
        expand=1,
        on_click=plus_click
    )

    minusButton = ft.ElevatedButton(
        text="-",
        bgcolor=ft.colors.BLUE_GREY_100,
        color=ft.colors.BLACK,
        expand=1,
        on_click=minus_click
    )

    calcButton = ft.ElevatedButton(
        text="Calcular",
        bgcolor=ft.colors.BLUE_GREY_100,
        color=ft.colors.BLACK,
        expand=4,
        on_click=calc_click
    )

    eraseButton = ft.ElevatedButton(
        text="Borrar",
        bgcolor=ft.colors.BLUE_GREY_100,
        color=ft.colors.BLACK,
        expand=2,
        on_click=erase_click
    )

    resultText = ft.Text(
        value=" ", 
        expand=1,

    )
    cText = ft.Container(
        content=resultText,
        bgcolor=ft.colors.BLUE_GREY_100,
        expand=1,
        height=204
    )

    buttonRow = ft.Row(spacing=5, controls=[plusButton, sizeCont, minusButton, calcButton, eraseButton])
    r = contentTabConvertor(3)
    r.append(cText)
    matrixRow = ft.Row(spacing=10, controls=r, alignment=ft.alignment.center) 
    column = ft.Column(controls=[matrixRow, buttonRow], spacing=20)
    controls = ft.Container(content=column)


    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Convertor",
                content=ft.Text("a")
            ),
            ft.Tab(
                text="Gauss-Jordan",
                content=controls
            ),
        ],
        expand=1,
    )
    
    page.add(t)

def contentTabConvertor(n):
    matrizInput = ft.DataTable(
            width=100*n,
            height=68*n,
            border=ft.border.all(1, "black"),
            columns=[],
            rows=[],
        )
    
    for i in range(1, n+1):
        matrizInput.columns.append(ft.DataColumn(ft.Text("x" + str(i)), numeric=True))
    
    for i in range(0, n):
        matrizInput.rows.append(ft.DataRow(cells=[]))
        for j in range(0, n):
            matrizInput.rows[i].cells.append(ft.DataCell(ft.TextField("0", border_width=0, keyboard_type=ft.KeyboardType.NUMBER)))
    
    matrizBInput = ft.DataTable(
            width=100,
            height=68*n,
            border=ft.border.all(1, "red"),
            columns=[ft.DataColumn(ft.Text("b"), numeric=True)],
            rows=[],
        )
    
    for i in range(0, n):
        matrizBInput.rows.append(ft.DataRow(cells=[ft.DataCell(ft.TextField("0", border_width=0, keyboard_type=ft.KeyboardType.NUMBER))]))

    return [matrizInput, matrizBInput]

def gJordan(a, b):
    try:
        return np.linalg.solve(a, b)
    except:
        return "La matriz A es singular, por lo que no se puede resolver"

ft.app(main)