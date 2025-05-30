aws secretsmanager create-secret \
    --name "google-service-account" \
    --secret-string "$(cat secrets/service-account.json)"
