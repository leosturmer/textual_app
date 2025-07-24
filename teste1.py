from textual.app import App, ComposeResult
from textual.widgets import Label, TextArea, Header, Footer, Button, Input


class AppTeste(App):

    CSS_PATH = 'teste1.tcss'

    def compose(self):
        yield Label('''Aqui é o texto da área. Uau. Louco isso.
                    
        Aqui vai ser uma lojinha. Estou fingindo ser uma lojinha.
        Você pode cadastrar produtos na lojinha.
                       
        ''', classes='box')

        yield Input('Digite o nome do produto: ')
        yield Input('Digite o valor do produto: ')

        yield Button('Confirmar', id='Confirmar')
        yield Button('Cancelar', id='Cancelar')


    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button))
        

if __name__ == "__main__":
    app = AppTeste()
    app.run()