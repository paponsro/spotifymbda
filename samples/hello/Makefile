FUNCTION_NAME?=hello_get
PROJECT:=bigdataupv-2020
REGION:=europe-west2
FUNCTION_URL:=https://$(REGION)-$(PROJECT).cloudfunctions.net/$(FUNCTION_NAME)

include ../common.mk

.PHONY: test_curl
test_curl: ## Sends a sample request using cURL
	curl -w'\n' -X POST $(FUNCTION_URL) \
		-H "Content-Type: application/json" \
		-d '{"name":"Mike"}'

PHONY: test_httpie
test_httpie: ## Sends a sample request using HTTPie
	http -v $(FUNCTION_URL) name=Mike

