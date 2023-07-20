#! /bin/bash
echo "Cual es tu nombre?"
read name
if [ $name ]; then
	echo "$name sounds good to me"
else
	echo "Wow, No me gusta"
fi