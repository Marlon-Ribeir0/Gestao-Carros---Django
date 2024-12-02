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

<h2>Contribuindo</h2>
<p>Se você deseja contribuir com o projeto, siga os seguintes passos:</p>
<ul>
    <li>Fork este repositório.</li>
    <li>Crie uma branch para suas modificações: <code>git checkout -b minha-modificacao</code></li>
    <li>Faça suas alterações e commit: <code>git commit -am 'Adicionando uma nova funcionalidade'</code></li>
    <li>Envia para o repositório original: <code>git push origin minha-modificacao</code></li>
    <li>Abra um pull request.</li>
</ul>
