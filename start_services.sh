cd app/

# Start rasa server with nlu model

rasa run actions --actions actions -vv --model models --enable-api --cors "*" --debug -p $PORT