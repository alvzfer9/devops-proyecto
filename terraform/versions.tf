terraform {
  backend "azurerm" {
    resource_group_name  = "reg-terraform-state"
    storage_account_name = "tfstatedevops28799"
    container_name       = "tfstate"
    key                  = "devops-academia.tfstate"
  }

  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.80"
    }
  }
}

provider "azurerm" {
  features {}
}