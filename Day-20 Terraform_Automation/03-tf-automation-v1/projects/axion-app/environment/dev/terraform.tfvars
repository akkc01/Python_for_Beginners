subscription_id = "b8e77924-89da-41ce-8257-846989faab77"

rg_name       = "jarvis-dev-eastus-rg"
location      = "East US"
vnet_name     = "jarvis-dev-eastus-vnet"
address_space = ["10.20.0.0/16"]

tags = {
  environment = "dev"
  application = "axion"
  owner       = "devops"
  cost_center = "engineering"
}