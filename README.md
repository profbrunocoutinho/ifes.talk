# ifes.talk
---

Chatbot do Instituto Federal do ES - assistente virtual para os alunos, servidores e comunidade em geral.

* **Branch master**: código estável;
* **Branch develop**: código de uma release.

# Pré-requisitos

* Rasa - https://rasa.com/docs/rasa/user-guide/installation/

* Rasa X - https://rasa.com/docs/rasa-x/installation-and-setup/install/local-mode/

# Compilação e Testes do Ifes.talk

* Execute um fork no projeto principal.

* No Windows você pode usar o PowerShell para a compilação e teste do bot, já no Linux use o Terminal.

* No diretório principal do projeto, já em sua máquina:

1. Execute o treinamento do NLU

* rasa train nlu -vv
* rasa train -vv

2. Valide os dados e realize testes iniciais

* rasa data validate -vv
* rasa test --out results/
* rasa test nlu --out results/results-nlu-test
* rasa test core --fail-on-prediction-errors --out results/results-core-test

3. Rode o servidor local para executar as actions:

* rasa run actions --actions actions -vv

4. Executando o Rasa X:

* Em outro terminal Powershell, no mesmo diretório principal do projeto, execute **rasa x**

5. Testando o ifes.talk

* Na tela do browser aberta pelo Rasa X você um web chat. No menu esquerdo você terá o local para simular uma conversa com o bot, dentre outras opções como: histórico de conversas, gráficos, treinamento do bot, etc...
