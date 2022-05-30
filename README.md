
# 💻 K-2S0 API

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

Uma API Rest para comunicação e persistência dos meus bots K-2SO. Até o momento, temos duas versões:

* Bot para discord
* Bot para telegram

Ambos utilizam automações e eventos para otimizar meu dia. Essa API é um centralizador de algumas informações que constituem o ecosistema dos bots.

### Buildando e rodando

Esse projeto utiliza [Docker](https://www.docker.com/) para virtualização do ambiente. Todas as dependencias são copiadas para dentro do container, e então instaladas. Posteriormente, copiamos todos os outros arquivos e inicializamos a aplicação. Para executá-la localmente, primeiro você precisará construir a imagem:

```sh
docker build -t csorgo/k2soAPI .
```

Após o build, basta executar o container:

```sh
docker run csorgo/k2soAPI -p 80
```

## Primeiros passos

### Pré requisitos

### Instalação