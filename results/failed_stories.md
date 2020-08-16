## happy path 1 (C:\Users\bccou\AppData\Local\Temp\tmp5u7kz3sf\e1a2ba0f19b044ebbe00464467ed7ebd_conversation_tests.md)
* greet: hello there!   <!-- predicted: mood_great: hello there! -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_great: amazing   <!-- predicted: deny: amazing -->
    - utter_happy   <!-- predicted: utter_goodbye -->


## happy path 2 (C:\Users\bccou\AppData\Local\Temp\tmp5u7kz3sf\e1a2ba0f19b044ebbe00464467ed7ebd_conversation_tests.md)
* greet: hello there!   <!-- predicted: mood_great: hello there! -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_great: amazing   <!-- predicted: deny: amazing -->
    - utter_happy   <!-- predicted: utter_goodbye -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (C:\Users\bccou\AppData\Local\Temp\tmp5u7kz3sf\e1a2ba0f19b044ebbe00464467ed7ebd_conversation_tests.md)
* greet: hello   <!-- predicted: mood_great: hello -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_unhappy: not good   <!-- predicted: goodbye: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help
* affirm: yes   <!-- predicted: goodbye: yes -->
    - utter_happy   <!-- predicted: utter_goodbye -->


## sad path 2 (C:\Users\bccou\AppData\Local\Temp\tmp5u7kz3sf\e1a2ba0f19b044ebbe00464467ed7ebd_conversation_tests.md)
* greet: hello   <!-- predicted: mood_great: hello -->
    - utter_greet   <!-- predicted: utter_happy -->
* mood_unhappy: not good   <!-- predicted: goodbye: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help
* deny: not really   <!-- predicted: bot_challenge: not really -->
    - utter_goodbye   <!-- predicted: utter_iamabot -->


## sad path 3 (C:\Users\bccou\AppData\Local\Temp\tmp5u7kz3sf\e1a2ba0f19b044ebbe00464467ed7ebd_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: goodbye: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help
* deny: no
    - utter_goodbye


