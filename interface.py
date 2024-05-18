import json
import requests

def menu():
    print("\n=== Menu ===")
    print("1. Inserir funcionário")
    print("2. Excluir funcionário")
    print("3. Listar funcionários")
    print("4. Atualizar funcionário")
    print("5. Consultar inventário de um funcionário")
    print("6. Inserir ativo notebook")
    print("7. Atualizar informações do ativo notebook")
    print("8. Excluir ativo notebook")
    print("9. Inserir ativo monitor")
    print("10. Atualizar informações do ativo monitor")
    print("11. Excluir ativo monitor")
    print("12. Inserir ativo teclado")
    print("13. Atualizar informações do ativo teclado")
    print("14. Excluir ativo teclado")
    print("15. Inserir ativo mouse")
    print("16. Atualizar informações do ativo mouse")
    print("17. Excluir ativo mouse")
    print("18. Inserir ativo nobreak")
    print("19. Atualizar informações do ativo nobreak")
    print("20. Excluir ativo nobreak")
    print("21. Inserir ativo headset")
    print("22. Atualizar informações do ativo headset")
    print("23. Excluir ativo headset")
    print("24. Inserir ativo desktop")
    print("25. Atualizar informações do ativo desktop")
    print("26. Excluir ativo desktop")
    print("27. Inserir ativo celular")
    print("28. Atualizar informações do ativo celular")
    print("29. Excluir ativo celular")
    print("30. Inserir ativo acessórios")
    print("31. Atualizar informações do ativo acessórios")
    print("32. Excluir ativo acessórios")
    print("33. Sair")

#
# Funcionário
#
def inserir_funcionario():
    cpf = input("Digite o CPF do funcionário: ")
    nome = input("Digite o nome do funcionário: ")
    response = requests.post('http://localhost:5000/funcionario', json={'cpf': cpf, 'nome': nome})
    print(json.dumps(response.json(), indent=4))

def excluir_funcionario():
    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
    response = requests.delete(f'http://localhost:5000/funcionario/{cpf}')
    print(json.dumps(response.json(), indent=4))

def listar_funcionarios():
    response = requests.get('http://localhost:5000/funcionario')
    print(json.dumps(response.json(), indent=4))

def atualizar_funcionario():
    cpf = input("Digite o CPF do funcionário que deseja atualizar o nome: ")
    nome = input("Digite o novo nome do funcionário: ")
    response = requests.put(f'http://localhost:5000/funcionario/{cpf}', json={'nome': nome})
    print(json.dumps(response.json(), indent=4))

def consultar_inventario():
    cpf = input("Digite o CPF do funcionário que deseja consultar o inventário: ")
    response = requests.get(f'http://localhost:5000/funcionario/{cpf}')
    print(json.dumps(response.json(), indent=4))

#
# Notebook
#
def inserir_notebook():
    cpf = input("Digite o CPF do funcionário: ")
    tag = input("Digite a TAG do notebook: ")
    modelo = input("Digite o modelo do notebook: ")
    n_serie = input("Digite o número de série do notebook: ")
    versao_so = input("Digite a versão do sistema operacional do notebook: ")
    caracteristicas = input("Digite as características do notebook: ")
    observacoes = input("Digite observações sobre o notebook: ")
    response = requests.post('http://localhost:5000/notebook', json={'cpf': cpf, 'tag': tag, 'modelo': modelo, 'n_serie': n_serie, 'versao_so': versao_so, 'caracteristicas': caracteristicas, 'observacoes': observacoes})
    print(json.dumps(response.json(), indent=4))

def atualizar_notebook():
    tag = input("Digite a TAG do notebook que deseja atualizar: ")
    cpf = input("Digite o CPF do funcionário: ")
    modelo = input("Digite o novo modelo do notebook: ")
    n_serie = input("Digite o novo número de série do notebook: ")
    versao_so = input("Digite a nova versão do sistema operacional do notebook: ")
    caracteristicas = input("Digite as novas características do notebook: ")
    observacoes = input("Digite as novas observações sobre o notebook: ")
    response = requests.put(f'http://localhost:5000/notebook/{tag}', json={'cpf': cpf, 'tag': tag, 'modelo': modelo, 'n_serie': n_serie, 'versao_so': versao_so, 'caracteristicas': caracteristicas, 'observacoes': observacoes})
    print(json.dumps(response.json(), indent=4))

def excluir_notebook():
    tag = input("Digite a TAG do notebook que deseja excluir: ")
    response = requests.delete(f'http://localhost:5000/notebook/{tag}')
    print(json.dumps(response.json(), indent=4))

#
# Monitor
#
def inserir_monitor():
    cpf = input("Digite o CPF do funcionário: ")
    tag = input("Digite a TAG do monitor: ")
    marca = input("Digite a marca do monitor: ")
    modelo = input("Digite o modelo do monitor: ")
    n_serie = input("Digite o número de série do monitor: ")
    response = requests.post('http://localhost:5000/monitor', json={'cpf': cpf, 'tag': tag, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def atualizar_monitor():
    tag = input("Digite a TAG do monitor que deseja atualizar: ")
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a nova marca do monitor: ")
    modelo = input("Digite o novo modelo do monitor: ")
    n_serie = input("Digite o novo número de série do monitor: ")
    response = requests.put(f'http://localhost:5000/monitor/{tag}', json={'cpf': cpf, 'tag': tag, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def excluir_monitor():
    tag = input("Digite a TAG do monitor que deseja excluir: ")
    response = requests.delete(f'http://localhost:5000/monitor/{tag}')
    print(json.dumps(response.json(), indent=4))

#
# Teclado
#
def inserir_teclado():
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a marca do teclado: ")
    modelo = input("Digite o modelo do teclado: ")
    n_serie = input("Digite o número de série do teclado: ")
    response = requests.post('http://localhost:5000/teclado', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def atualizar_teclado():
    n_serie = input("Digite o número de série do teclado que deseja atualizar: ")
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a nova marca do teclado: ")
    modelo = input("Digite o novo modelo do teclado: ")
    response = requests.put(f'http://localhost:5000/teclado/{n_serie}', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def excluir_teclado():
    n_serie = input("Digite o número de série do teclado que deseja excluir: ")
    response = requests.delete(f'http://localhost:5000/teclado/{n_serie}')
    print(json.dumps(response.json(), indent=4))

#
# Mouse
#
def inserir_mouse():
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a marca do mouse: ")
    modelo = input("Digite o modelo do mouse: ")
    n_serie = input("Digite o número de série do mouse: ")
    response = requests.post('http://localhost:5000/mouse', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def atualizar_mouse():
    n_serie = input("Digite o número de série do mouse que deseja atualizar: ")
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a nova marca do mouse: ")
    modelo = input("Digite o novo modelo do mouse: ")
    response = requests.put(f'http://localhost:5000/mouse/{n_serie}', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def excluir_mouse():
    n_serie = input("Digite o número de série do mouse que deseja excluir: ")
    response = requests.delete(f'http://localhost:5000/mouse/{n_serie}')
    print(json.dumps(response.json(), indent=4))

#
# Nobreak
#
def inserir_nobreak():
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a marca do nobreak: ")
    modelo = input("Digite o modelo do nobreak: ")
    n_serie = input("Digite o número de série do nobreak: ")
    response = requests.post('http://localhost:5000/nobreak', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def atualizar_nobreak():
    n_serie = input("Digite o número de série do nobreak que deseja atualizar: ")
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a nova marca do nobreak: ")
    modelo = input("Digite o novo modelo do nobreak: ")
    response = requests.put(f'http://localhost:5000/nobreak/{n_serie}', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def excluir_nobreak():
    n_serie = input("Digite o número de série do nobreak que deseja excluir: ")
    response = requests.delete(f'http://localhost:5000/nobreak/{n_serie}')
    print(json.dumps(response.json(), indent=4))

#
# Headset
#
def inserir_headset():
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a marca do headset: ")
    modelo = input("Digite o modelo do headset: ")
    n_serie = input("Digite o número de série do headset: ")
    response = requests.post('http://localhost:5000/headset', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def atualizar_headset():
    n_serie = input("Digite o número de série do headset que deseja atualizar: ")
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a nova marca do headset: ")
    modelo = input("Digite o novo modelo do headset: ")
    response = requests.put(f'http://localhost:5000/headset/{n_serie}', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'n_serie': n_serie})
    print(json.dumps(response.json(), indent=4))

def excluir_headset():
    n_serie = input("Digite o número de série do headset que deseja excluir: ")
    response = requests.delete(f'http://localhost:5000/headset/{n_serie}')
    print(json.dumps(response.json(), indent=4))

#
# Celular
#
def inserir_celular():
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a marca do celular: ")
    modelo = input("Digite o modelo do celular: ")
    imei1 = input("Digite o IMEI do celular: ")
    numero = input("Digite o número do celular: ")
    response = requests.post('http://localhost:5000/celular', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'imei1': imei1, 'numero': numero})
    print(json.dumps(response.json(), indent=4))

def atualizar_celular():
    imei1 = input("Digite o IMEI do celular que deseja atualizar: ")
    cpf = input("Digite o CPF do funcionário: ")
    marca = input("Digite a nova marca do celular: ")
    modelo = input("Digite o novo modelo do celular: ")
    numero = input("Digite o novo número do celular: ")
    response = requests.put(f'http://localhost:5000/celular/{imei1}', json={'cpf': cpf, 'marca': marca, 'modelo': modelo, 'imei1': imei1, 'numero': numero})
    print(json.dumps(response.json(), indent=4))

def excluir_celular():
    imei1 = input("Digite o IMEI do celular que deseja excluir: ")
    response = requests.delete(f'http://localhost:5000/celular/{imei1}')
    print(json.dumps(response.json(), indent=4))

#
# Acessórios
#
def inserir_acessorios():
    cpf = input("Digite o CPF do funcionário: ")
    suporte_notebook = input("Digite a quantidade de suportes de notebook: ")
    mouse_pad = input("Digite a quantidade de mouse pads: ")
    response = requests.post('http://localhost:5000/acessorios', json={'cpf': cpf, 'suporte_notebook': suporte_notebook, 'mouse_pad': mouse_pad})
    print(json.dumps(response.json(), indent=4))

def atualizar_acessorios():
    cpf = input("Digite o CPF do funcionário que deseja atualizar os acessórios: ")
    suporte_notebook = input("Digite a nova quantidade de suportes de notebook: ")
    mouse_pad = input("Digite a nova quantidade de mouse pads: ")
    response = requests.put(f'http://localhost:5000/acessorios/{cpf}', json={'cpf': cpf, 'suporte_notebook': suporte_notebook, 'mouse_pad': mouse_pad})
    print(json.dumps(response.json(), indent=4))

def excluir_acessorios():
    cpf = input("Digite o CPF do funcionário que deseja excluir os acessórios: ")
    response = requests.delete(f'http://localhost:5000/acessorios/{cpf}')
    print(json.dumps(response.json(), indent=4))

#
# Desktop
#
def inserir_desktop():
    cpf = input("Digite o CPF do funcionário: ")
    modelo = input("Digite o modelo do desktop: ")
    tag = input("Digite a TAG do desktop: ")
    n_serie = input("Digite o número de série do desktop: ")
    versao = input("Digite a versão do desktop: ")
    caracteristicas = input("Digite as características do desktop: ")
    observacoes = input("Digite as observações do desktop: ")

    data = {
        'cpf': cpf,
        'modelo': modelo,
        'tag': tag,
        'n_serie': n_serie,
        'versao': versao,
        'caracteristicas': caracteristicas,
        'observacoes': observacoes
    }

    response = requests.post('http://localhost:5000/desktop', json=data)
    print(response.json()['message'])

def atualizar_desktop():
    tag = input("Digite a TAG do desktop que deseja atualizar: ")
    cpf = input("Digite o novo CPF do funcionário: ")
    modelo = input("Digite o novo modelo do desktop: ")
    n_serie = input("Digite o novo número de série do desktop: ")
    versao = input("Digite a nova versão do desktop: ")
    caracteristicas = input("Digite as novas características do desktop: ")
    observacoes = input("Digite as novas observações do desktop: ")

    data = {
        'cpf': cpf,
        'modelo': modelo,
        'tag': tag,
        'n_serie': n_serie,
        'versao': versao,
        'caracteristicas': caracteristicas,
        'observacoes': observacoes
    }

    response = requests.put(f'http://localhost:5000/desktop/{tag}', json=data)
    print(response.json()['message'])

def excluir_desktop():
    tag = input("Digite a TAG do desktop que deseja excluir: ")
    response = requests.delete(f'http://localhost:5000/desktop/{tag}')
    print(response.json()['message'])


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        inserir_funcionario()
    elif opcao == '2':
        excluir_funcionario()
    elif opcao == '3':
        listar_funcionarios()
    elif opcao == '4':
        atualizar_funcionario()
    elif opcao == '5':
        consultar_inventario()

    elif opcao == '6':
        inserir_notebook()
    elif opcao == '7':
        atualizar_notebook()
    elif opcao == '8':
        excluir_notebook()

    elif opcao == '9':
        inserir_monitor()
    elif opcao == '10':
        atualizar_monitor()
    elif opcao == '11':
        excluir_monitor()

    elif opcao == '12':
        inserir_teclado()
    elif opcao == '13':
        atualizar_teclado()
    elif opcao == '14':
        excluir_teclado()

    elif opcao == '15':
        inserir_mouse()
    elif opcao == '16':
        atualizar_mouse()
    elif opcao == '17':
        excluir_mouse()

    elif opcao == '18':
        inserir_nobreak()
    elif opcao == '19':
        atualizar_nobreak()
    elif opcao == '20':
        excluir_nobreak()

    elif opcao == '21':
        inserir_headset()
    elif opcao == '22':
        atualizar_headset()
    elif opcao == '23':
        excluir_headset()

    elif opcao == '24':
        inserir_desktop()
    elif opcao == '25':
        atualizar_desktop()
    elif opcao == '26':
        excluir_desktop()

    elif opcao == '27':
        inserir_celular()
    elif opcao == '28':
        atualizar_celular()
    elif opcao == '29':
        excluir_celular()

    elif opcao == '30':
        inserir_acessorios()
    elif opcao == '31':
        atualizar_acessorios()
    elif opcao == '32':
        excluir_acessorios()

    elif opcao == '33':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
