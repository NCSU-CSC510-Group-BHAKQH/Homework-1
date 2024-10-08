#!/bin/bash

pid=$(pgrep -f infinite.sh | head -n 1); [ -n "$pid" ] && kill "$pid" && echo "Process infinite.sh with PID $pid has been killed." || echo "No running process found for infinite.sh."
