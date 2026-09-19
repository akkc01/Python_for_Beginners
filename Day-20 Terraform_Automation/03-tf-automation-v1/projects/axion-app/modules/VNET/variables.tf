variable "vnet_name" {
  description = "The name of the virtual network"
  type        = string
  default     = "example-virtual-network"
}

variable "location" {
  description = "The location of the resource group"
  type        = string
  default     = "East US"
}

variable "rg_name" {
  description = "The name of the resource group"
  type        = string
  default     = "example-resource-group"
}

variable "address_space" {
  description = "The address space of the virtual network"
  type        = list(string)
  default     = ["10.10.0.0/16"]
}

variable "tags" {
  description = "Resource tags"
  type        = map(string)
  default     = {}
}