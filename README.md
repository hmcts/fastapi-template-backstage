# fastapi-template-backstage

A [Backstage](https://backstage.io) scaffolder template for creating new HMCTS Python FastAPI microservices.

## Usage

This template is registered in the HMCTS Backstage catalog. To use it:

1. Go to the Backstage portal
2. Click **Create** → **FastAPI Service**
3. Fill in the form and click **Create**

Backstage will create a new GitHub repository under `hmcts/` with all files pre-configured.

## Local development

To modify this template:

1. Edit `template.yaml` to change the form parameters or scaffolder steps
2. Edit files in `skeleton/` to change what gets generated
3. Use `${{ values.xxx }}` (Nunjucks) for dynamic values — see `template.yaml` for available variables

## Application Insights

The generated service uses the [HMCTS Python base image](https://github.com/hmcts/cnp-python-base), which has Azure Application Insights pre-wired via OpenTelemetry — no application code changes are required.

### Environment variables

| Variable | Required | Description |
|---|---|---|
| `APPLICATIONINSIGHTS_CONNECTION_STRING` | One of these two | The App Insights connection string directly. |
| `APPLICATIONINSIGHTS_CONNECTION_STRING_FILE` | One of these two | Path to a file containing the connection string (recommended for cluster deployments). |
| `OTEL_SERVICE_NAME` | Optional | Labels telemetry with the service name. Defaults to `unknown_service`. |
| `APPLICATIONINSIGHTS_LOGGER_NAMESPACE` | Optional | Logger namespace whose logs are forwarded to App Insights. Defaults to `uvicorn`. Set to `""` to capture all logs. |
| `OTEL_PYTHON_EXCLUDED_URLS` | Optional | Comma-separated URL patterns to exclude from tracing. Defaults to `health,readiness,liveness`. |

In HMCTS clusters, mount the connection string from Key Vault as a file and point `APPLICATIONINSIGHTS_CONNECTION_STRING_FILE` at it to keep the secret out of git.

Leave both connection string variables unset and telemetry is disabled — local development is unaffected.

For full details see the [cnp-python-base Application Insights documentation](https://github.com/hmcts/cnp-python-base#application-insights).

## Reference

- [template-spring-boot](https://github.com/hmcts/template-spring-boot) — Java equivalent
- [fastapi-template-github](https://github.com/hmcts/fastapi-template-github) — GitHub template equivalent (manual setup)
- [Backstage Scaffolder docs](https://backstage.io/docs/features/software-templates/)
