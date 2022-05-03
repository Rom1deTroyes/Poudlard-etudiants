#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <file>"
    exit 1
fi
docker exec -i mongodb sh -c 'mongoimport -u=root -p=root --authenticationDatabase admin -d ecole -c etudiants ' < "$1"
