module "rg" {
  source   = "../../modules/RG"
  rg_name  = var.rg_name
  location = var.location
}


module "vnet" {
  depends_on    = [module.rg]
  source        = "../../modules/VNET"
  vnet_name     = var.vnet_name
  location      = var.location
  rg_name       = var.rg_name
  address_space = var.address_space
}