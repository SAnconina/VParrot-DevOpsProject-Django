resource "kubernetes_config_map_v1" "vparrot_demo" {
  metadata {
    name      = "vparrot-terraform-demo"
    namespace = "vparrot"
  }

  data = {
    APP_NAME    = "VParrot"
    ENVIRONMENT = "development"
    MANAGED_BY  = "Terraform"
  }
}