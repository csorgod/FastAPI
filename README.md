
# 💻 PetAPI

<details>
  <summary>Conteúdo</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre o projeto</a>
      <ul>
        <li><a href="#built-with">Buildando e rodando</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Primeiros passos</a>
      <ul>
        <li><a href="#prerequisites">Pré requisitos</a></li>
        <li><a href="#installation">Instalação</a></li>
      </ul>
    </li>
  </ol>
</details>

## Sobre o projeto

Uma API Rest para persistência de informações sobre pets. Aqui, você pode cadastrar, consultar, alterar ou excluir o cadastro de um pet de forma simples e fácil através de uma requisição HTTP.

### Buildando e rodando

Esse projeto utiliza [Docker](https://www.docker.com/) para virtualização do ambiente. Todas as dependencias são copiadas para dentro do container, e então instaladas. Posteriormente, copiamos todos os outros arquivos e inicializamos a aplicação. Para executá-la localmente, primeiro você precisará construir a imagem:

```sh
docker build -t csorgo/PetAPI .
```

Após o build, basta executar o container:

```sh
docker run csorgo/PetAPI -p 80
```

## Primeiros passos

Ainda nada!

### Pré requisitos

Ainda nenhum!

### Instalação

Não é necessário ainda!
