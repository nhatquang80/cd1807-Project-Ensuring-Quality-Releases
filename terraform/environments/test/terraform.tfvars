# Azure subscription vars
subscription_id = "${env.ARM_SUBSCRIPTION_ID}"
client_id = "${env.ARM_CLIENT_ID}"
client_secret = "${env.ARM_CLIENT_SECRET}"
tenant_id = "${env.ARM_TENANT_ID}"

# Resource Group/Location
location = "eastus"
resource_group_name = "udacity-rg"
application_type = "udacity"

# Network
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"
