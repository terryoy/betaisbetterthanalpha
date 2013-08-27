#!/bin/sh

read proc_entry < .pid_entry
read proc_relay < .pid_relay
kill -9 $proc_entry $proc_relay
