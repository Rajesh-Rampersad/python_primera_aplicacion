class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, endereco, telefone=None):
        self.nome = nome
        self.categoria = categoria
        self.endereco = endereco
        self.telefone = telefone
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} - {self.categoria} - {self.endereco} - {self.telefone} - {'Ativo' if self.ativo else 'Inativo'}"

  # Listar restuarantes

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante.nome} - {restaurante.categoria} - {restaurante.endereco} - {restaurante.telefone} {'Ativo' if restaurante.ativo else 'Inativo'}")


restaurante1 = Restaurante(
    "Pizzaria do João", "Pizzaria", "Rua das Flores, 123", "1234-5678")
restaurante2 = Restaurante(
    "Churrascaria do Zé", "Churrascaria", "Avenida Brasil, 456", "9876-5432")
restaurante3 = Restaurante("Sushi do Carlos", "Sushi",
                           "Rua do Peixe, 789", "5555-5555")
# ejectar o método listar_restaurantes
Restaurante.listar_restaurantes()
