provider "azurerm" {
  features {}
  version = "~> 4.56.0"
}

resource "azurerm_resource_group" "example" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_api_management" "example" {
  name                = "example-apim"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  publisher_name      = "examplepublisher"
  publisher_email     = "pub@example.com"
  sku_name            = "Developer_1"
}

resource "azurerm_logic_app_workflow" "example" {
  name                = "example-workflow"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacc"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_app_service" "policy_management" {
  name                = "policy-management"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  app_service_plan_id = azurerm_app_service_plan.example.id
}

resource "azurerm_app_service" "claims_tracking" {
  name                = "claims-tracking"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  app_service_plan_id = azurerm_app_service_plan.example.id
}

resource "azurerm_app_service_plan" "example" {
  name                = "example-plan"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku {
    tier = "Basic"
    size = "B1"
  }
}
