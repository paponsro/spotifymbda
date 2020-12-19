FUNCTION_NAME?=hello_firestore
PROJECT:=bigdataupv-2020
REGION:=europe-west2
FUNCTION_URL:=https://$(REGION)-$(PROJECT).cloudfunctions.net/$(FUNCTION_NAME)
DEPLOY_PARAMS:=--region $(REGION)

include ../common.mk

.PHONY: sample_request
sample_request: ## Sends a sample request to a function
	http -v $(FUNCTION_URL) pokemonId=pikachu

