class GerenciadorEventos:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, nome, data):
        evento = {
            'nome': nome,
            'data': data
        }
        self.eventos.append(evento)
        print(f'Evento "{nome}" adicionado para o dia {data}.')

    def listar_eventos(self):
        if not self.eventos:
            print("Nenhum evento agendado.")
            return
        
        print("Eventos agendados:")
        for evento in self.eventos:
            print(f'Nome: {evento["nome"]}, Data: {evento["data"]}')

    def remover_evento(self, nome):
        evento_para_remover = None
        for evento in self.eventos:
            if evento['nome'] == nome:
                evento_para_remover = evento
                break
        
        if evento_para_remover:
            self.eventos.remove(evento_para_remover)
            print(f'Evento "{nome}" removido.')
        else:
            print(f'Evento "{nome}" não encontrado.')

def menu():
    gerente = GerenciadorEventos()
    
    while True:
        print("\nGerenciador de Eventos")
        print("1. Adicionar evento")
        print("2. Listar eventos")
        print("3. Remover evento")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome do evento: ")
            data = input("Digite a data do evento (dd/mm/aaaa): ")
            gerente.adicionar_evento(nome, data)
        elif escolha == '2':
            gerente.listar_eventos()
        elif escolha == '3':
            nome = input("Digite o nome do evento que deseja remover: ")
            gerente.remover_evento(nome)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
