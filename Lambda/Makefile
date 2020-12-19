FUNCTION_NAME?=resources_id
PROJECT:=spotifymbda
REGION:=europe-west2
FUNCTION_URL:=https://europe-west2-spotifymbda.cloudfunctions.net/resources_id
BUCKET_NAME:=spotifymbda
DEPLOY_PARAMS:=--set-env-vars BUCKET_NAME=$(BUCKET_NAME) --region $(REGION)


include ./common.mk

.PHONY: create_bucket
create_bucket: ## Creates the bucket needed for samples
	gsutil mb -c regional -l $(REGION) gs://$(BUCKET_NAME)

list_bucket: ## List bucket contents
	gsutil ls gs://$(BUCKET_NAME)

.PHONY: sample_request
sample_request: ## Sends a sample request to a function
	http -v $(FUNCTION_URL) pokemonId=charmander