# ${{ values.product }}-${{ values.component }}

${{ values.description }}

The application exposes health endpoints at `http://localhost:${{ values.http_port }}/health/readiness` and `http://localhost:${{ values.http_port }}/health/liveness`.

## Running locally

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) then:

```bash
uv sync --extra dev
uv run uvicorn app.main:app --reload --port ${{ values.http_port }}
```

The service will be available at `http://localhost:${{ values.http_port }}`.

## Running locally via Docker

> **Note:** The Dockerfile uses an HMCTS internal base image from `hmctsprod.azurecr.io`. You must be logged in to the registry (`az acr login --name hmctsprod`) before building.

```bash
docker build -t ${{ values.component }} .
docker run -p ${{ values.http_port }}:${{ values.http_port }} ${{ values.component }}
```

## Health endpoints

Your service must expose:

- `GET /health/readiness` — return HTTP 200 when ready to receive traffic
- `GET /health/liveness` — return HTTP 200 when the process is alive

## Running tests

```bash
uv run pytest tests/unit -v          # unit tests
uv run pytest tests/smoke -v         # smoke tests (requires TEST_URL env var)
uv run pytest tests/functional -v    # functional tests (requires TEST_URL env var)
```

## Application Insights

To enable Azure Application Insights telemetry, uncomment the two lines in `app/main.py` and add `azure-monitor-opentelemetry` to `pyproject.toml`. Set the `APPLICATIONINSIGHTS_CONNECTION_STRING` environment variable at runtime.

## Database (PostgreSQL)

To enable PostgreSQL, uncomment the `postgresql` block in `charts/${{ values.product }}-${{ values.component }}/values.yaml` and add your database config to the `environment` section.

## Jenkins

This service uses the HMCTS Jenkins shared library. Follow the [new component setup guide](https://hmcts.github.io/cloud-native-platform/new-component/github-repo.html) to register your service.
