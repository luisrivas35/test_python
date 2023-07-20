#!/bin/bash
SKILL="shell scripting"
echo "I want to be great at ${SKILL}. That's why I practice ${SKILL}."
hostname
date
uname -r
uname -m
df -h
if [[ "${UID}" -eq 0 ]]
then
  echo "You are root"
else
  echo "You are not root"
fi
