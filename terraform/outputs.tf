output "ecr_repository_url" {
  value = aws_ecr_repository.app.repository_url
}

output "alb_dns_name" {
  value = aws_lb.app.dns_name
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.main.name

}
output "rds_endpoint" {
  value = aws_db_instance.postgres.address
}

output "rds_db_name" {
  value = aws_db_instance.postgres.db_name
}