# Azure subscription vars
subscription_id = "${TF_VAR_subscription_id}"
client_id = "${TF_VAR_client_id}"
client_secret = "${TF_VAR_client_secret}"
tenant_id = "${TF_VAR_tenant_id}"

# Resource Group/Location
location = "eastus"
resource_group = "udacity-rg"
application_type = "udacity"

# Network
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"

# VM
vm_admin_username = "admin"
