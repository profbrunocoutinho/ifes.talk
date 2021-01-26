# ifes.talk 2.1.10
---

Chatbot do Instituto Federal do Espírito Santo - assistente virtual para os alunos, servidores e comunidade em geral. Atualmente em migração para o Rasa
Core. Atualização dos RODs (técnico, graduação e pós-graduação) na base de conhecimento do chatbot. Acréscimos referentes aos processos seletivos para a
comunidade em geral.

* **Branch master**: código estável 2.x;
* **Branch 2.x.y**: código em desenvolvimento de uma nova versão. Sofrerá merge na master após aprovação do coordenador.

# Pré-requisitos

* Rasa - https://rasa.com/docs/rasa/installation/

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

4. Testando o ifes.talk

* rasa shell
