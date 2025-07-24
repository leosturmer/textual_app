from textual.app import App, ComposeResult
from textual.widgets import Label, TextArea, Header, Footer, Button, Input, ListView, ListItem, Static
from textual.screen import Screen

############################################################################################################

########### Programa principal ###########

class Loja(App):
    ########### Coisas do programa ###########
    LISTA_DE_PRODUTOS = {}

    CSS_PATH = 'loja.tcss'

    ##########################################

    def compose(self) -> ComposeResult:
        yield Static('''
Loja de artigos legais
                     
O que deseja fazer?                     
                     
                     ''')

        yield Button('Cadastrar produto', id='bt_TelaCadastrar')
        yield Button('Editar produto', id='bt_TelaEditar')
        yield Button('Ver produtos cadastrados', id='bt_TelaVisualizar')

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'bt_TelaCadastrar':
            self.push_screen(CadastroProdutos())

        if event.button.id == 'bt_TelaEditar':
            pass 

        
        if event.button.id == 'bt_TelaVisualizar':
            pass


        # lista_items = ListView(
        #     ListItem(Label(self.items)))

    ########### Métodos programa ###########

    def limpar_formulario(self):
        for text in self.query('Input'):
            text.value = ''

    def voltar_tela(self):
        app.pop_screen()
    

############################################################################################################

########### Telas programa ###########


class CadastroProdutos(Screen):
    def compose(self):
        yield Static('''
Tela de cadastro de produtos em Textual
                     
''')
        yield Label('Produto: ')
        yield Input(id='tx_nome')

        yield Label('Preço: ')
        yield Input(id='tx_preco')

        yield Label('Quantidade: ')
        yield Input(id='tx_quantidade')
        
        yield Label('Descrição: ')
        yield Input(id='tx_descricao')

        yield Button('Limpar', id='bt_limpar')
        yield Button('Cadastrar', id='bt_CadastrarProduto')
        yield Button('Voltar', id='bt_voltar')


    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'bt_limpar':
            Loja.limpar_formulario(self)

        if event.button.id == 'bt_CadastrarProduto':
            nome = self.query_one('#tx_nome', Input).value
            preco = float(self.query_one('#tx_preco', Input).value)
            quantidade = int(self.query_one('#tx_quantidade', Input).value)
            descricao = self.query_one('#tx_descricao', Input).value

            Loja.LISTA_DE_PRODUTOS[nome] = {"preco": preco, "quantidade": quantidade, "descrição": descricao}

            Loja.limpar_formulario(self)
            self.notify(f'{Loja.LISTA_DE_PRODUTOS.keys()}')

        if event.button.id == 'bt_voltar':
            Loja.voltar_tela(app)

############################################################################################################





############################################################################################################


########### Início do programa ###########

if __name__ == '__main__':
    app = Loja()
    cadastro = CadastroProdutos()
    app.run()