variable "rg_name" {
  description = "The name of the resource group"
  type        = string
  default     = "example-resource-group"
}


variable "location" {
  description = "The location of the resource group"
  type        = string
  default     = "East US"
}

variable "tags" {
  description = "Resource tags"
  type        = map(string)
  default     = {}
}