# Teste de Automação para QA - CI&T

Olá! Bom dia, boa tarde ou boa noite!

Este é um desafio criado para a nossa seleção de uma pessoa Engenheira de Software que irá atuar na role de QA. 
Leia atentamente todo o conteúdo desse documento antes de começar qualquer execução!

Iremos utilizar o site https://automacaocombatista.herokuapp.com/treinamento/home para realizar nosso teste, onde faremos alguns cenários utilizando a linguagem Gherkin.
À princípio, daremos um modelo para que você apenas crie os passos da automação. Depois, será necessário criar um teste baseado numa descrição de negócio.
Por fim, você terá que criar um cenário que ache adequado para a situação. As descrições detalhadas dos passos estarão mais abaixo.
O teste pode ser feito em qualquer linguagem de programação e com qualquer framework de teste de interface. Fica a seu critério escolher o que se adequa mais
ao seu perfil e/ou ao seu conhecimento.
A entrega desse teste pode ser feita através de um arquivo .zip ou .rar com os arquivos ou pode ser através de um link de seu Git pessoal (por exemplo).

O que iremos avaliar:
- Organização de código, arquitetura e boas práticas de programação
- Criação de casos de testes utilizando Gherkin
- Utilização de algum padrão de desenvolvimento de automação
- Como foi a utilização do framework de automação e da linguagem de programação
- Estruturação de relatórios (diferencial)
- Facilidade na execução dos testes (por exemplo, utilização do Docker)(diferencial)

Qualquer dúvida que tenha, basta entrar em contato conosco que teremos o maior prazer em te ajudar!

## Primeira parte
Temos o seguinte cenário, escrito em Gherkin, que devemos automatizar:

**Funcionalidade:** Editar usuário<br>
**Cenário:** Editar o primeiro usuário que esteja na lista de usuários<br>
**Dado** que acessei a tela de listagem de usuários<br>
**E** que acionei a edição do primeiro usuário da lista<br>
**Quando** altero seu nome e sua universidade<br>
**E** concluo a alteração<br>
**Então** visualizo as informações do usuário alterado<br>

Você irá agora pegar esse cenário e realizar a automação dele no site passado anteriormente (a lista de usuários está no lado esquerdo, em **Formulário**).

## Segunda parte
Agora, estamos com a seguinte informação de nova funcionalidade que temos que testar para o cliente:

>Construímos uma funcionalidade nova de excluir usuário e gostaria que você testasse esse cenário. A ideia é excluir o primeiro usuário da lista, para podermos saber se está realmente funcionando.

Com essa informação em mãos, vamos para a codificação desse cenário de teste. Leve em consideração a codificação feita previamente e tente escrever o cenário em Gherkin antes de começar qualquer codificação.


## Terceira parte
Por fim, você terá que criar um cenário novo que não foi descrito anteriormente. Pense bem no que gostaria de testar! A ideia aqui é realmente ver como você faria um cenário do zero! Abuse e use da codificação feita anteriormente para te ajudar!


## Considerações finais
Por fim, é isso o teste! Espero que tenha conseguido fazer tudo e que tenha feito com bastante carinho e atenção! Aguardamos ansiosamente pelo seu envio e, assim que avaliarmos o teste, iremos te dar um retorno com feedbacks a respeito!
Esperamos também que tenha gostado e que tenha aprendido um pouco conosco!
Até breve!

