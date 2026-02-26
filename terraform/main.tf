provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_app_service_plan" "asp" {
  name                = "appserviceplan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_app_service" "app" {
  name                = "appservice"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.asp.id
}

resource "azurerm_cdn_profile" "example" {
  name                = "exampleCDNProfile"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard_Verizon"
}

resource "azurerm_cdn_endpoint" "example" {
  name                = "exampleCDNEndpoint"
  profile_name        = azurerm_cdn_profile.example.name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  origin {
    name      = "example"
    host_name = azurerm_app_service.app.default_site_hostname
  }
}

resource "azurerm_function_app" "fa" {
  name                = "functionapp"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.asp.id
  storage_account_name = azurerm_storage_account.sa.name
  storage_account_access_key = azurerm_storage_account.sa.primary_access_key
  version            = "~3"
}

resource "azurerm_storage_account" "sa" {
  name                     = "examplestorageacc"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_api_management" "apim" {
  name                = "exampleAPImanagement"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  publisher_name      = "MyCompany"
  publisher_email     = "company@example.com"
  sku_name            = "Developer_1"
}

resource "azurerm_monitor_diagnostic_setting" "ads" {
  name                           = "example-diagnostic-setting"
  target_resource_id             = azurerm_app_service.app.id
  log_analytics_workspace_id     = azurerm_log_analytics_workspace.law.id
  enabled_log {
    category = "AppServiceHTTPLogs"
  }
  metric {
    category = "AllMetrics"
  }
}

resource "azurerm_log_analytics_workspace" "law" {
  name                = "example-law"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
}
