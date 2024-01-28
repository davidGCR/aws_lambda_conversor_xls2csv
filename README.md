# AWS Lambda para conversion XLSX a CSV

Lambda function para convertir un XLSX en S3 a CSV usando:
[![awslambda](https://img.shields.io/badge/aws_lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white&labelColor=101010)]()
[![amazons3](https://img.shields.io/badge/amazons3-569A31?style=for-the-badge&logo=amazons3&logoColor=white&labelColor=101010)]()
[![terraform](https://img.shields.io/badge/terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white&labelColor=101010)]()
[![docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=101010)]()

## 1. Empezando
Siga las siguientes instrucciones para la ejecucion y pruebas del codigo.

### 1.1 Prerequisitos

Requerimientos para ejecutar el codigo
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Terraform](https://developer.hashicorp.com/terraform/downloads?product_intent=terraform)
- Docker

### 1.2 Instalacion Prerequisitos
- Instalar AWS ClI y configure el perfil default con el Access Key. Verifique la instalacion con el siguiente comando en un terminal.
        
        aws --version

- Instalar Terraform. Verifique la instalacion con el siguiente comando en un terminal.

        terraform --version
- Instalar Docker
  
## 2. Despliegue

- Ejecute el dockerfile para generar el lambda empaquetado
- Suba el empaquetado a S3 y agreguelo a un lambda
