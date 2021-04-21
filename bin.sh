if [ $1 == "test" ]
then
  poetry run pytest --cov-report term-missing --cov=dogelib tests/
elif [ $1 == "fix" ]
then
  poetry run isort .
else
  echo "Command not registered"
fi