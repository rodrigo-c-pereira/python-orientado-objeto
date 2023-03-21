class Cliente:
    def __init__(self, nome, telefone, plano, email):
        self.nome = nome
        self.telefone = telefone
        self.lista_planos = ['basic', 'plus', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido') 
        self.email = email
         
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme}")
        elif self.plano == 'premium':
            print(f"Ver filme {filme}")
        elif self.plano == 'basic' and plano_filme == 'premium':
            print("Faça o upgrade para premium para assistir este filme")
        else:
            print("Plano inválido")





perfil_cliente = Cliente('Rodrigo Pereira', '123-456', 'basic', 'rodrigo@outlook.com')
print(perfil_cliente.email)
print(perfil_cliente.plano)
perfil_cliente.ver_filme("Creed", "premium")
perfil_cliente.mudar_plano("premium")
print(perfil_cliente.plano)
perfil_cliente.ver_filme("Creed", "premium")