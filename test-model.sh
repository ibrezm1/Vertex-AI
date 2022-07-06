#gcloud auth application-default login

ENDPOINT_ID="2942213951091376128"
PROJECT_ID="zeta-yen-319702"
INPUT_DATA_FILE="sampleinput.json"

curl \
-X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/endpoints/${ENDPOINT_ID}:predict \
-d "@${INPUT_DATA_FILE}"

