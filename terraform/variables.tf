variable "resource_group_name" {
  description = "The name of the resource group in which to create the resources"
  type        = string
}

variable "resource_group_location" {
  description = "The Azure region where the resources will be created"
  type        = string
}

variable "sql_admin_username" {
  description = "The administrator username for SQL Server"
  type        = string
}

variable "sql_admin_password" {
  description = "The administrator password for SQL Server"
  type        = string
  sensitive   = true
}
