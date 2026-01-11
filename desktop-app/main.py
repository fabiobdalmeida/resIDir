import flet as ft

def main(page: ft.Page):
    page.title = "resIDir - Gestão de Comprovantes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def btn_click(e):
        page.add(ft.Text("Botão clicado! Preparando geração de PDF..."))

    # Layout simples
    page.add(
        ft.Column(
            [
                ft.Text("Bem-vindo ao resIDir", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Gere comprovantes de residência válidos a partir de contas compartilhadas."),
                ft.ElevatedButton("Gerar Novo Comprovante", on_click=btn_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)