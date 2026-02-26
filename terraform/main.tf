provider "azurerm" {
  features {}
  version = "~> 4.56.0"
}

resource "azurerm_resource_group" "rg" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_api_management" "apim" {
  name                = "example-apim"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  publisher_name      = "Example Publisher"
  publisher_email     = "publisher@example.com"
  sku_name            = "Developer_1"
}

resource "azurerm_api_management_api" "example_api" {
  name                = "example-api"
  resource_group_name = azurerm_resource_group.rg.name
  api_management_name = azurerm_api_management.apim.name
  revision            = "1"
  display_name        = "Example API"
  path                = "example"
  protocols           = ["https"]
}

resource "azurerm_api_management_api_operation" "get" {
  operation_id        = "get"
  api_name            = azurerm_api_management_api.example_api.name
  api_management_name = azurerm_api_management.apim.name
  resource_group_name = azurerm_resource_group.rg.name
  display_name        = "GET Example"
  method              = "GET"
  url_template        = "/"
  response {
    status       = 200
    description  = "OK"
  }
}

resource "azurerm_b2c_directory" "example" {
  name                = "example-directory"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    name                = "Basic"
    capacity           = 1
  }
}
