#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## greet + goodbye
* greet: Ei!
  - utter_greet
* bye: tchau
  - utter_bye

## greet + thanks
* greet: Ei ifes.talk
  - utter_greet
* thank: obrigado
  - utter_noworries

## greet + thanks + goodbye
* greet: Olá!
  - utter_greet
* thank: obrigado
  - utter_noworries
* bye: bye bye
  - utter_bye