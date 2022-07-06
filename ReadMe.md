[![Open In Colab](img/colab.svg)](https://colab.research.google.com/drive/1RupAVB60jXwPt4i72isuA2aSZojNDVcm#scrollTo=dFjRJMivbEtx)


Refering the article by Piyush on Vertex AI [here](https://medium.com/@piyushpandey282/model-serving-at-scale-with-vertex-ai-custom-container-deployment-with-pre-and-post-processing-12ac62f4ce76)
Move to a better article by chavez should handle retraining as well[here](https://medium.com/@jchavezar/ml-from-local-to-production-vertex-ai-d3b09998008c)



Latex Cheatsheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Test Model Development
* TODO : Apply preprocessing and post processing 
* TODO : Move the Jupyter Notebook here

Temp Collab - zip model and get that [here](https://colab.research.google.com/drive/1RupAVB60jXwPt4i72isuA2aSZojNDVcm#scrollTo=Ccr2VxwXiQwd)

docker build --tag=test .

docker run -p 5005:5005 --name=test test 

curl -X GET http://localhost:5005/healthz

Run disposable container and check code is faster
docker run --rm -it --entrypoint bash test
apt install nano

gcloud beta artifacts repositories create testrepo \
 --repository-format=docker \
 --location=us-central1 \
 --project=zeta-yen-319702

curl -X POST -d "@sampleinput.json" -H "Content-Type: application/json" http://localhost:5005/predict

docker tag test us-central1-docker.pkg.dev/zeta-yen-319702/testrepo/test

docker push us-central1-docker.pkg.dev/zeta-yen-319702/testrepo/test

gcloud beta ai models upload \
  --region=us-central1 \
  --display-name=custom \
  --container-image-uri=us-central1-docker.pkg.dev/zeta-yen-319702/testrepo/test \
  --container-ports=5005 \
  --container-health-route=/healthz \
  --container-predict-route=/predict \
 --project=zeta-yen-319702

 Set degault project via cloud 

 gcloud beta ai models list \
  --region=us-central1 \
  --filter=display_name=custom

Learn about 
gcloud alpha interactive

gcloud config set project zeta-yen-319702
gcloud config set compute/region us-central1 

gcloud beta ai endpoints create \
  --region=us-central1  \
  --display-name=customeend

gcloud beta ai endpoints deploy-model 2942213951091376128 \
  --region=us-central1 \
  --model=7839513507996368896 \
  --display-name=custom \
  --machine-type=n1-standard-2 \
  --min-replica-count=1 \
  --max-replica-count=1 \
  --traffic-split=0=100 


