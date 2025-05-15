import os
import time
import requests

# Set your Vault server URL
vault_url = "https://vault.camfu.co"

while True:
    print("Checking Vault server health...")
    # Check the status of the Vault server
    response = requests.get(f"{vault_url}/v1/sys/health")

    # If the server is not reporting a 200 status code, unseal it
    if response.status_code != 200:
        # Get your unseal key from an environment variable
        unseal_key = os.getenv("VAULT_UNSEAL_KEY")

        # Send a POST request to unseal the Vault server
        unseal_response = requests.post(f"{vault_url}/v1/sys/unseal", json={"key": unseal_key})

        # Check the response
        if unseal_response.status_code == 200:
            print("Vault server unsealed successfully.")
        else:
            print("Failed to unseal Vault server.")
    else:
        print("Vault server is healthy.")

    # Wait for 15 minutes
    time.sleep(15 * 60)