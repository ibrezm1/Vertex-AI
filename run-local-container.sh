#bash script


docker stop test
docker rm test
docker rmi -f test

docker build --tag=test .
docker run -p 5005:5005 --name test  test

# docker exec -it test bash

# curl -X POST -d "@sampleinput.json" -H "Content-Type: application/json" http://localhost:5005/predict

