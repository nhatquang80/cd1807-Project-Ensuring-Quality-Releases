#!/bin/bash

RESOURCE_GROUP_NAME="udacity-rg"
STORAGE_ACCOUNT_NAME="udacitytfstate$RANDOM"
CONTAINER_NAME="tfstate"

SUBSCRIPTION_ID=$(az account show --query id --output tsv)

# Create resource group
az group create --name $RESOURCE_GROUP_NAME --location eastus

# Create storage account
az storage account create --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --sku Standard_LRS --encryption-services blob

# Get storage account key
ACCOUNT_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP_NAME --account-name $STORAGE_ACCOUNT_NAME --query '[0].value' -o tsv)

export ARM_ACCESS_KEY=$ACCOUNT_KEY
export ARM_SUBSCRIPTION_ID=$SUBSCRIPTION_ID

# Create blob container
az storage container create --name $CONTAINER_NAME --account-name $STORAGE_ACCOUNT_NAME --account-key $ACCOUNT_KEY

echo "RESOURCE_GROUP_NAME=$RESOURCE_GROUP_NAME"
echo "STORAGE_ACCOUNT_NAME=$STORAGE_ACCOUNT_NAME"
echo "CONTAINER_NAME=$CONTAINER_NAME"
echo "ACCOUNT_KEY=$ACCOUNT_KEY"

