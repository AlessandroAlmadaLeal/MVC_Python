# Exercicio MVC - Python

A atividade consiste em aprender o MVC em um cenário hipotético para auxiliar na fixação dos conceitos abordados em sala de aula.

Estarei replicando o conteúdo de um vídeo do youtube do canal "Programador Lhama". Ele apresentou o cenceito de maneira concisa e direta, digo isso comparado às aulas formais da UNIVESP. Nos vídeos ele aplicou a arquitetura MVC na tecnologia de meu interesse (linguagem Python) utilizando apenas funções built-ins da linguagem (livre de frameworks).

A ideia é ter um ponto de partida para meus estudos em demais tecnologias de mercado como C#, Java, Rust, GoLang e etc... Reforçando, esta é proxêmica prática inicial neste assunto a ideia é copiar código manualmente da tela.

## O que é a arquitetura MVC?

MVC é um acrônimo para Model-View-Controller (Modelo-Visão-Controlador), um padrão arquitetural amplamente utilizado no desenvolvimento de software, especialmente em aplicações web e mobile.

Ele separa a aplicação em três **componentes** interconectados, cada um com uma responsabilidade específica, promovendo organização, manutenibilidade e escalabilidade do código.

## Componentes do MVC

- Model (Modelo): Representa os dados da aplicação e a lógica de negócios. Ele interage com o banco de dados (se houver), processa os dados e define as regras de negócio. O Modelo não se preocupa com a forma como os dados são apresentados ao usuário. Em resumo, o Modelo é o coração da aplicação, onde os dados são gerenciados e manipulados.

- View (Visão): É a interface com o usuário. Ela exibe os dados do Modelo de uma forma amigável e permite a interação do usuário com a aplicação. A Visão não contém nenhuma lógica de negócios, apenas a lógica de apresentação. Ela recebe os dados do Controlador e os exibe para o usuário. Exemplos de Visão podem ser páginas HTML, telas de aplicativos mobile ou componentes de interface gráfica.

- Controller (Controlador): Atua como um intermediário entre o Modelo e a Visão. Ele recebe as requisições do usuário (como cliques em botões, envios de formulários, etc.), processa essas requisições, interage com o Modelo para obter ou atualizar os dados e, em seguida, seleciona a Visão apropriada para exibir os resultados ao usuário. O Controlador contém a lógica de controle do fluxo da aplicação.

## Como o MVC funciona na prática

Segue abaixo um recurso visual para apoio das descrições a seguir:

![Medium.com](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ZqwogJDz1cA1sr-B.png)

Como exemplo, vamos adotar uma consulta simples ao banco de dados, por ser um procedimento onde se envia uma instrução de consulta para obter dados no retorno o procedimento é ilustrado com mais clareza.

### Setinhas de ida no diagrama

1. O usuário interage com a interface, nesse caso a view (visão), clicando em um link ou enviando um formulário.

2. A requisição é encaminhada para o controller (controlador) correspondente.

3. Este controller (controlador) processa a requisição, solicitando dados do model (modelo).

4. O model (modelo) realiza o acesso ao banco de dados e soilicita as consultas etc.

### Setinhas de volta no diagrama

1. O banco de dados retorna ao model (modelo) que irá processar os dados conforme as regras de negócio estabelecidas.  

2. Ao finalizar suas atividades o model (modelo) então retorna para o controller (controlador) os dados da consulta.

3. O controller (controlador) seleciona a view (visão) apropriada e passa os dados para ela.

4. A view (visão) exibe os dados formatados para o usuário.

O que seria transmitido no caminho de retorno ao usuário, muitas vezes muda de uma operação para outra do CRUD. Por exemplo, uma inserção de dados no banco, nos "caminhos de volta" ilustrados do diagrama só carregaria uma mensagem de OK (sucesso, 200 e etc.) ou NOK de cada um dos modulos e o motivo claramanete de acordo com o módulo violado (500, 403, 401 e etc.).

## Vantagens do uso do MVC

O uso do padrão MVC traz diversas vantagens significativas para o desenvolvimento de software.

Promove a **separação de responsabilidades**, onde cada componente (Modelo, Visão e Controlador) possui uma função clara e bem definida. Essa divisão facilita o desenvolvimento, a manutenção e a testabilidade do código, tornando o processo mais eficiente e menos propenso a erros.

O MVC favorece a **reusabilidade** de código. Os componentes independentes, podem ser reutilizados em diferentes partes da mesma aplicação ou até mesmo em outros projetos, economizando tempo e esforço de desenvolvimento.

A estrutura modular do MVC contribui para a **organização e escalabilidade** do código. Cada módulo pode ser replicado em diferentes servidores, otimizando o uso de recursos e aumentando a disponibilidade e a tolerância a falhas. Isso significa que, à medida que a demanda aumenta, você pode adicionar mais servidores e distribuir os módulos entre eles, garantindo que a aplicação continue funcionando mesmo com alta carga ou falha de um servidor. Nesse contexto, por exemplo poderiamos ter servidores dedicados para processar requisições de usuário (Controladores) e outros para acessar o banco de dados (Modelo).

Simplifica o **entendimento e a manutenção**, um software organizado e desacoplado e também permite que ela cresça de forma mais organizada e sustentável, suportando novas funcionalidades e demandas com mais facilidade.

Dito tudo isso, cabe acrescentar que o MVC facilita o trabalho em equipe, permitindo que desenvolvedores trabalhem em diferentes componentes simultaneamente, sem interferir no trabalho uns dos outros. Isso agiliza o processo de desenvolvimento e melhora a **colaboração** entre os membros da equipe.

## Referencias

- PROGRAMADOR LHAMA. Padrão MVC em Python 1 - Introdução. YouTube, 16 ago. 2021. Disponível em: <https://www.youtube.com/watch?v=abqeIMr1hsg&list=PLAgbpJQADBGKvsjOu4gHU5E9WUQs8XRgS>. Acesso em: 28 dez. 2024.

- NORMANDO, Célio. Arquitetura MVC e princípios de projeto. Medium, 2023. Disponível em: <https://medium.com/@celionormando/arquitetura-mvc-e-princ%C3%ADpios-de-projeto-3d0b278ef910>. Acesso em: 28 dez. 2024.

- GOOGLE AI. Apresentando o Gemini: o modelo de última geração do Google para tudo. Blog do Google AI, Mountain View, CA, 6 dez. 2023. Disponível em: <https://gemini.google.com/>. Acesso em: 28 dez. 2024.
