if [ $1 == "test" ]
then
  pytest --cov-report term-missing --cov=dogelib tests/
elif [ $1 == "fix" ]
then
  isort .
else
  echo "Command not registered"
fi