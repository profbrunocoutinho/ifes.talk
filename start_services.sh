# Start rasa server with nlu model

rasa train --force
rasa run --model models --enable-api --cors "*" --debug -p $PORT
