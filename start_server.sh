#!/bin/sh

# start entry server
nohup python entry.py >> logs/http.log & echo $! > .pid_entry

# start relay server
nohup python relay.py >> logs/relay.log & echo $! > .pid_relay
