<h1 align="center">Sistema de Gestão de Vendas de Carros (SGVC)</h1>

<p>Bem-vindo ao Sistema de Gestão de Vendas de Carros (SGVC), um projeto desenvolvido em Django e Bootstrap 5 para facilitar o gerenciamento de vendas de carros. Este README fornece informações essenciais sobre como configurar e executar o projeto em seu ambiente local.</p>

<h2>Requisitos</h2>
<p>Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:</p>
<ul>
    <li><strong>Python</strong> (versão recomendada: 3.7 ou superior)</li>
    <li><strong>Django</strong> (será instalado automaticamente ao seguir as instruções abaixo)</li>
    <li>Outras dependências listadas no arquivo <code>requirements.txt</code></li>
</ul>

<h2>Instalação das Dependências</h2>
<p>Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>Rodar o Projeto</h2>
<p>Após instalar as dependências, aplique as migrações no banco de dados com o comando:</p>
<pre><code>python manage.py migrate</code></pre>

<p>Agora o projeto já pode ser inicializado com o comando:</p>
<pre><code>python manage.py runserver</code></pre>

<p>O servidor estará rodando localmente em <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a>.</p>

<h2>Funcionalidades</h2>
<ul>
    <li><strong>Cadastro de carros</strong> para venda, com informações como marca, modelo, ano, preço e descrição.</li>
    <li><strong>Gerenciamento de clientes</strong>, com registros de informações como nome, telefone e email.</li>
    <li><strong>Registro de vendas</strong>, permitindo a vinculação de carros vendidos aos clientes.</li>
    <li><strong>Interface responsiva</strong>, utilizando o Bootstrap 5 para garantir uma experiência de usuário otimizada tanto em dispositivos móveis quanto desktop.</li>
</ul>

<h2>Imagens do Projeto</h2>
<p>Abaixo estão algumas imagens do Sistema de Gestão de Vendas de Carros:</p>


<img src="https://imgur.com/a/oEMmZAl" alt="Imagem 1" width="500px">
<img src="https://imgur.com/HCL99pF" alt="Imagem 2" width="500px">

<h2>Cadastro de Marcas</h2>
<p>Para cadastrar uma nova marca de carro no sistema, acesse o painel de administração do Django. Siga os passos abaixo:</p>

<ol>
    <li>Acesse o painel de administração em <a href="http://127.0.0.1:8000/admin" target="_blank">http://127.0.0.1:8000/admin</a> com o superusuário.</li>
    <li>Na seção "Marcas de Carros", clique em "Adicionar marca".</li>
    <li>Preencha o formulário com o nome e a descrição da marca e clique em "Salvar".</li>
</ol>

<p>Exemplo de como o formulário de cadastro de marcas aparece no painel de administração:</p>
<img src="caminho/para/imagem-marcas.png" alt="Cadastro de Marcas" width="500px">

<h2>Cadastro de Usuários</h2>
<p>Para cadastrar novos usuários (clientes ou administradores), siga os passos abaixo:</p>

<ol>
    <li>Acesse a seção "Usuários" no painel de administração.</li>
    <li>Clique em "Adicionar usuário".</li>
    <li>Preencha o nome, email, senha e outros campos necessários e clique em "Salvar".</li>
    <li>Após criar o usuário, você pode adicionar permissões de administrador ou associar o usuário a um grupo.</li>
</ol>

<p>Exemplo de como o formulário de cadastro de usuários aparece no painel de administração:</p>
<img src="caminho/para/imagem-usuarios.png" alt="Cadastro de Usuários" width="500px">

<h2>Cadastro de Carros</h2>
<p>Para cadastrar um carro no sistema, siga os seguintes passos:</p>

<ol>
    <li>Acesse a seção "Carros" no painel de administração.</li>
    <li>Clique em "Adicionar carro".</li>
    <li>Preencha as informações do carro, como marca, modelo, ano, preço e descrição. Depois, clique em "Salvar".</li>
</ol>

<p>Exemplo de como o formulário de cadastro de carros aparece no painel de administração:</p>
<img src="caminho/para/imagem-cadastro-carro.png" alt="Cadastro de Carros" width="500px">

<h2>Detalhes do Carro</h2>
<p>Após cadastrar um carro, você pode visualizar e editar seus detalhes. Abaixo está um exemplo de como os detalhes de um carro aparecem no painel de administração:</p>
<img src="caminho/para/imagem-detalhes-carro.png" alt="Detalhes do Carro" width="500px">

