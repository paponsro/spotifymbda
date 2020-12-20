FUNCTION_NAME?=resources_firestore
PROJECT:=spotifymbda
REGION:=europe-west2
FUNCTION_URL:=https://europe-west2-spotifymbda.cloudfunctions.net/resources_firestore
BUCKET_NAME:=spotifymbda
DEPLOY_PARAMS:=--set-env-vars BUCKET_NAME=$(BUCKET_NAME) --region $(REGION)  --project $(PROJECT) 


include ./common.mk


.PHONY: sample_request
sample_request: ## Sends a sample request to a function
	http -v $(FUNCTION_URL)
	resource_id= RES.001