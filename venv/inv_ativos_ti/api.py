from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['inv_ativos_ti']

funcionario = db['funcionario'] 
notebook = db['notebook'] 
monitor = db['monitor'] 
teclado = db['teclado']
mouse = db['mouse']
desktop = db['desktop']
acessorios = db['acessorios']
nobreak = db['nobreak']
headset = db['headset']
celular = db['celular']

# Verifica se o CPF tem 11 dígitos
def validar_cpf(cpf):
    return len(cpf) == 11

# Inserir um novo funcionário
@app.route('/funcionario', methods=['POST'])
def inserir_funcionario():
    data = request.json
    cpf = data.get('cpf', '')
    nome = data.get('nome', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    if funcionario.find_one({'_id': cpf}):
        return jsonify({'message': 'CPF já cadastrado'}), 400

    funcionario.insert_one({'_id': cpf, 'nome': nome})
    return jsonify({'message': 'Funcionário inserido com sucesso'}), 201

# Excluir um funcionário pelo CPF
@app.route('/funcionario/<cpf>', methods=['DELETE'])
def excluir_funcionario(cpf):
    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF inválido'}), 400

    result = funcionario.delete_one({'_id': cpf})
    if result.deleted_count == 0:
        return jsonify({'message': 'Funcionário não encontrado'}), 404

    return jsonify({'message': 'Funcionário excluído com sucesso'}), 200

# Listar todos os funcionários
@app.route('/funcionario', methods=['GET'])
def listar_funcionarios():
    funcionarios = list(funcionario.find({}, {'_id': 1, 'nome': 1}))
    return jsonify(funcionarios), 200

# Atualizar o nome do funcionário pelo CPF
@app.route('/funcionario/<cpf>', methods=['PUT'])
def atualizar_nome(cpf):
    data = request.json
    nome = data.get('nome', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF inválido'}), 400

    result = funcionario.update_one({'_id': cpf}, {'$set': {'nome': nome}})
    if result.matched_count == 0:
        return jsonify({'message': 'Funcionário não encontrado'}), 404

    return jsonify({'message': 'Nome do funcionário atualizado com sucesso'}), 200

# Consultar o inventario completo de um funcionário
@app.route('/funcionario/<cpf>', methods=['GET'])
def retornar_funcionario_com_ativos(cpf):
    funcionario_ = funcionario.find_one({'_id': cpf})
    if not funcionario_:
        return jsonify({'message': 'Funcionário não encontrado'}), 404

    # Removendo o campo '_id' dos documentos, pois dá o erro: "TypeError: Object of type ObjectId is not JSON serializable"
    notebook_ = notebook.find_one({'cpf': cpf}, {'_id': False}) or {}
    monitor_ = list(monitor.find({'cpf': cpf}, {'_id': False})) or []
    teclado_ = teclado.find_one({'cpf': cpf}, {'_id': False}) or {}
    mouse_ = mouse.find_one({'cpf': cpf}, {'_id': False}) or {}
    desktop_ = desktop.find_one({'cpf': cpf}, {'_id': False}) or {}
    acessorios_ = acessorios.find_one({'cpf': cpf}, {'_id': False}) or {}
    nobreak_ = nobreak.find_one({'cpf': cpf}, {'_id': False}) or {}
    headset_ = headset.find_one({'cpf': cpf}, {'_id': False}) or {}
    celular_ = celular.find_one({'cpf': cpf}, {'_id': False}) or {}

    # Montando o retorno com o funcionário e seus ativos
    retorno = {
        'funcionario': funcionario_,
        'notebook': notebook_,
        'monitor': monitor_,
        'teclado': teclado_,
        'mouse': mouse_,
        'desktop': desktop_,
        'acessorios': acessorios_,
        'nobreak': nobreak_,
        'headset': headset_,
        'celular': celular_
    }

    return jsonify(retorno), 200

#
# Notebook
#

# Inserir ativo notebook
@app.route('/notebook', methods=['POST'])
def inserir_notebook():
    data = request.json
    cpf = data.get('cpf', '')
    tag = data.get('tag', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    versao_so = data.get('versao_so', '')
    caracteristicas = data.get('caracteristicas', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    # Restringe a apenas 1 notebook por funcionario
    if notebook.find_one({'cpf': cpf}):
        return jsonify({'message': 'Funcionario já possuí notebook'}), 400

    notebook.insert_one({
        'cpf': cpf,
        'tag': tag,
        'modelo': modelo,
        'n_serie': n_serie,
        'versao_so': versao_so,
        'caracteristicas': caracteristicas,
        'observacoes': observacoes
    })

    return jsonify({'message': 'Notebook inserido com sucesso'}), 201

# Atualizar as informações do ativo notebook (referência = TAG)
@app.route('/notebook/<tag>', methods=['PUT'])
def atualizar_notebook(tag):
    data = request.json
    cpf = data.get('cpf', '')
    tag = data.get('tag', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    versao_so = data.get('versao_so', '')
    caracteristicas = data.get('caracteristicas', '')
    observacoes = data.get('observacoes', '')

    result = notebook.update_one({'tag': tag}, {'$set': {
        'cpf': cpf,
        'tag': tag,
        'modelo': modelo,
        'n_serie': n_serie,
        'versao_so': versao_so,
        'caracteristicas': caracteristicas,
        'observacoes': observacoes
    }})

    if result.matched_count == 0:
        return jsonify({'message': 'Notebook não encontrado'}), 404

    return jsonify({'message': 'Notebook atualizado com sucesso'}), 200

# Limpar as informações do ativo notebook (referência = TAG)
@app.route('/notebook/<tag>', methods=['DELETE'])
def excluir_notebook(tag):
    result = notebook.delete_one({'tag': tag})
    if result.deleted_count == 0:
        return jsonify({'message': 'Notebook não encontrado'}), 404

    return jsonify({'message': 'Notebook excluído com sucesso'}), 200

#
# Monitor
#

# Inserir ativo monitor (referência = n_serie)
@app.route('/monitor', methods=['POST'])
def inserir_monitor():
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    # Restringe a apenas 2 monitores por funcionário
    if monitor.count_documents({'cpf': cpf}) == 2:
        return jsonify({'message': 'Funcionario já possuí dois monitores'}), 400

    monitor.insert_one({
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    })

    return jsonify({'message': 'Notebook inserido com sucesso'}), 201

# Atualizar as informações do ativo monitor (referência = n_serie)
@app.route('/monitor/<n_serie>', methods=['PUT'])
def atualizar_monitor(n_serie):
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    result = monitor.update_one({'n_serie': n_serie}, {'$set': {
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    }})

    if result.matched_count == 0:
        return jsonify({'message': 'Monitor não encontrado'}), 404

    return jsonify({'message': 'Monitor atualizado com sucesso'}), 200

# Limpar as informações do ativo monitor (referência = n_serie)
@app.route('/monitor/<n_serie>', methods=['DELETE'])
def excluir_monitor(n_serie):
    result = monitor.delete_one({'n_serie': n_serie})
    if result.deleted_count == 0:
        return jsonify({'message': 'Monitor não encontrado'}), 404

    return jsonify({'message': 'Monitor excluído com sucesso'}), 200

#
# Teclado
#

# Inserir ativo teclado
@app.route('/teclado', methods=['POST'])
def inserir_teclado():
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    # Restringe a apenas 1 teclado por funcionário
    if teclado.find_one({'cpf': cpf}):
        return jsonify({'message': 'Funcionario já possuí teclado'}), 400

    teclado.insert_one({
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    })

    return jsonify({'message': 'Teclado inserido com sucesso'}), 201

# Atualizar as informações do ativo teclado (referência = n_serie)
@app.route('/teclado/<n_serie>', methods=['PUT'])
def atualizar_teclado(n_serie):
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    result = teclado.update_one({'n_serie': n_serie}, {'$set': {
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    }})

    if result.matched_count == 0:
        return jsonify({'message': 'Teclado não encontrado'}), 404

    return jsonify({'message': 'Teclado atualizado com sucesso'}), 200

# Limpar as informações do ativo teclado (referência = n_serie)
@app.route('/teclado/<n_serie>', methods=['DELETE'])
def excluir_teclado(n_serie):
    result = teclado.delete_one({'n_serie': n_serie})
    if result.deleted_count == 0:
        return jsonify({'message': 'Teclado não encontrado'}), 404

    return jsonify({'message': 'Teclado excluído com sucesso'}), 200

#
# Mouse
#

# Inserir ativo mouse
@app.route('/mouse', methods=['POST'])
def inserir_mouse():
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    # Restringe a apenas 1 mouse por funcionário
    if mouse.find_one({'cpf': cpf}):
        return jsonify({'message': 'Funcionario já possuí mouse'}), 400

    mouse.insert_one({
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    })

    return jsonify({'message': 'Mouse inserido com sucesso'}), 201

# Atualizar as informações do ativo mouse (referência = n_serie)
@app.route('/mouse/<n_serie>', methods=['PUT'])
def atualizar_mouse(n_serie):
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    result = mouse.update_one({'n_serie': n_serie}, {'$set': {
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    }})

    if result.matched_count == 0:
        return jsonify({'message': 'Mouse não encontrado'}), 404

    return jsonify({'message': 'Mouse atualizado com sucesso'}), 200

# Limpar as informações do ativo mouse (referência = n_serie)
@app.route('/mouse/<n_serie>', methods=['DELETE'])
def excluir_mouse(n_serie):
    result = mouse.delete_one({'n_serie': n_serie})
    if result.deleted_count == 0:
        return jsonify({'message': 'Mouse não encontrado'}), 404

    return jsonify({'message': 'Mouse excluído com sucesso'}), 200

#
# Nobreak
#

# Inserir ativo nobreak
@app.route('/nobreak', methods=['POST'])
def inserir_nobreak():
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    # Restringe a apenas 1 nobreak por funcionário
    if nobreak.find_one({'cpf': cpf}):
        return jsonify({'message': 'Funcionario já possuí nobreak'}), 400

    nobreak.insert_one({
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    })

    return jsonify({'message': 'Mouse inserido com sucesso'}), 201

# Atualizar as informações do ativo nobreak (referência = n_serie)
@app.route('/nobreak/<n_serie>', methods=['PUT'])
def atualizar_nobreak(n_serie):
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    result = nobreak.update_one({'n_serie': n_serie}, {'$set': {
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    }})

    if result.matched_count == 0:
        return jsonify({'message': 'Nobreak não encontrado'}), 404

    return jsonify({'message': 'Nobreak atualizado com sucesso'}), 200

# Limpar as informações do ativo nobreak (referência = n_serie)
@app.route('/nobreak/<n_serie>', methods=['DELETE'])
def excluir_nobreak(n_serie):
    result = nobreak.delete_one({'n_serie': n_serie})
    if result.deleted_count == 0:
        return jsonify({'message': 'Nobreak não encontrado'}), 404

    return jsonify({'message': 'Nobreak excluído com sucesso'}), 200

#
# Headset
#

# Inserir ativo headset
@app.route('/headset', methods=['POST'])
def inserir_headset():
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    # Restringe a apenas 1 headset por funcionário
    if nobreak.find_one({'cpf': cpf}):
        return jsonify({'message': 'Funcionario já possuí headset'}), 400

    headset.insert_one({
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    })

    return jsonify({'message': 'Headset inserido com sucesso'}), 201

# Atualizar as informações do ativo headset
@app.route('/headset/<n_serie>', methods=['PUT'])
def atualizar_headset(n_serie):
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    n_serie = data.get('n_serie', '')
    observacoes = data.get('observacoes', '')

    result = headset.update_one({'n_serie': n_serie}, {'$set': {
        'cpf': cpf,
        'modelo': modelo,
        'n_serie': n_serie,
        'observacoes': observacoes
    }})

    if result.matched_count == 0:
        return jsonify({'message': 'Headset não encontrado'}), 404

    return jsonify({'message': 'Headset atualizado com sucesso'}), 200

# Limpar as informações do ativo headset
@app.route('/headset/<n_serie>', methods=['DELETE'])
def excluir_headset(n_serie):
    result = headset.delete_one({'n_serie': n_serie})
    if result.deleted_count == 0:
        return jsonify({'message': 'Headset não encontrado'}), 404

    return jsonify({'message': 'Headset excluído com sucesso'}), 200

#
# Desktop
#

# Inserir ativo desktop
@app.route('/desktop', methods=['POST'])
def inserir_desktop():
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    tag = data.get('tag', '')
    n_serie = data.get('n_serie', '')
    versao = data.get('versao', '')
    caracteristicas = data.get('caracteristicas', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    # Restringe a apenas 1 desktop por funcionário
    if desktop.find_one({'cpf': cpf}):
        return jsonify({'message': 'Funcionario já possuí desktop'}), 400

    desktop.insert_one({
        'cpf': cpf,
        'modelo': modelo,
        'tag': tag,
        'n_serie': n_serie,
        'versao': versao,
        'caracteristicas': caracteristicas,
        'observacoes': observacoes
    })

    return jsonify({'message': 'Desktop inserido com sucesso'}), 201

# Atualizar as informações do ativo desktop (referência = TAG)
@app.route('/desktop/<tag>', methods=['PUT'])
def atualizar_desktop(tag):
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    tag = data.get('tag', '')
    n_serie = data.get('n_serie', '')
    versao = data.get('versao', '')
    caracteristicas = data.get('caracteristicas', '')
    observacoes = data.get('observacoes', '')

    result = desktop.update_one({'tag': tag}, {'$set': {
        'cpf': cpf,
        'modelo': modelo,
        'tag': tag,
        'n_serie': n_serie,
        'versao': versao,
        'caracteristicas': caracteristicas,
        'observacoes': observacoes
    }})

    if result.matched_count == 0:
        return jsonify({'message': 'Desktop não encontrado'}), 404

    return jsonify({'message': 'Desktop atualizado com sucesso'}), 200

# Limpar as informações do ativo desktop (referência = TAG)
@app.route('/desktop/<tag>', methods=['DELETE'])
def excluir_desktop(tag):
    result = desktop.delete_one({'tag': tag})
    if result.deleted_count == 0:
        return jsonify({'message': 'Headset não encontrado'}), 404

    return jsonify({'message': 'Headset excluído com sucesso'}), 200

#
# Celular
#

# Inserir ativo celular
@app.route('/celular', methods=['POST'])
def inserir_celular():
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    imei1 = data.get('imei1', '')
    numero = data.get('numero', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    # Restringe a apenas 1 celular por funcionário
    if celular.find_one({'cpf': cpf}):
        return jsonify({'message': 'Funcionario já possuí celular'}), 400

    celular.insert_one({
        'cpf': cpf,
        'modelo': modelo,
        'imei1': imei1,
        'numero': numero,
        'observacoes': observacoes
    })

    return jsonify({'message': 'Celular inserido com sucesso'}), 201

# Atualizar as informações do ativo celular (referência = imei1)
@app.route('/celular/<imei1>', methods=['PUT'])
def atualizar_celular(imei1):
    data = request.json
    cpf = data.get('cpf', '')
    modelo = data.get('modelo', '')
    imei1 = data.get('imei1', '')
    numero = data.get('numero', '')
    observacoes = data.get('observacoes', '')

    result = celular.update_one({'imei1': imei1}, {'$set': {
        'cpf': cpf,
        'modelo': modelo,
        'imei1': imei1,
        'numero': numero,
        'observacoes': observacoes
    }})

    if result.matched_count == 0:
        return jsonify({'message': 'Celular não encontrado'}), 404

    return jsonify({'message': 'Celular atualizado com sucesso'}), 200

# Limpar as informações do ativo celular (referência = imei1)
@app.route('/celular/<imei1>', methods=['DELETE'])
def excluir_celular(imei1):
    result = celular.delete_one({'imei1': imei1})
    if result.deleted_count == 0:
        return jsonify({'message': 'Celular não encontrado'}), 404

    return jsonify({'message': 'Celular excluído com sucesso'}), 200

#
# Acessórios
#

# Inserir ativo acessórios
@app.route('/acessorios', methods=['POST'])
def inserir_acessorios():
    data = request.json
    cpf = data.get('cpf', '')
    suporte_notebook = data.get('suporte_notebook', '')
    mouse_pad = data.get('mouse_pad', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF deve conter 11 dígitos'}), 400

    # Restringe a apenas 1 acessorio de cada por funcionário

    sn = acessorios.find_one({'cpf': cpf}, {'suporte_notebook': suporte_notebook})
    mp = acessorios.find_one({'cpf': cpf}, {'mouse_pad': mouse_pad})

    if sn == 1 and suporte_notebook == 1:
        return jsonify({'message': 'Funcionario já possuí suporte de notebook'}), 400
    elif mp == 1 and mouse_pad == 1:
        return jsonify({'message': 'Funcionario já possuí mouse pad'}), 400

    acessorios.insert_one({
        'cpf': cpf,
        'suporte_notebook': suporte_notebook,
        'mouse_pad': mouse_pad,
        'observacoes': observacoes
    })

    return jsonify({'message': 'Celular inserido com sucesso'}), 201

# Atualizar as informações do ativo acessórios (referência = cpf)
@app.route('/acessorios/<cpf>', methods=['PUT'])
def atualizar_acessorios(cpf):
    data = request.json
    cpf = data.get('cpf', '')
    suporte_notebook = data.get('suporte_notebook', '')
    mouse_pad = data.get('mouse_pad', '')
    observacoes = data.get('observacoes', '')

    if not validar_cpf(cpf):
        return jsonify({'message': 'CPF inválido'}), 400
    
    if suporte_notebook > 1:
        return jsonify({'message': 'Só é permitido um suporte de notebook por funcionário'}), 400
    elif mouse_pad > 1:
        return jsonify({'message': 'Só é permitido um mouse pad por funcionário'}), 400

    result = acessorios.update_one({'cpf': cpf}, {'$set': {
        'cpf': cpf,
        'suporte_notebook': suporte_notebook,
        'mouse_pad': mouse_pad,
        'observacoes': observacoes
    }})

    if result.matched_count == 0:
        return jsonify({'message': 'Funcionário não possuí nenhum acessório'}), 404

    return jsonify({'message': 'Acessórios atualizados com sucesso'}), 200

# Limpar as informações do ativo acessórios (referência = cpf)
@app.route('/acessorios/<cpf>', methods=['DELETE'])
def excluir_acessorios(cpf):
    result = acessorios.delete_one({'cpf': cpf})
    if result.deleted_count == 0:
        return jsonify({'message': 'Funcionário não possui acessórios'}), 404

    return jsonify({'message': 'Acessórios excluídos com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)