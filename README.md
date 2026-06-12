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

## Reference

- [template-spring-boot](https://github.com/hmcts/template-spring-boot) — Java equivalent
- [fastapi-template-github](https://github.com/hmcts/fastapi-template-github) — GitHub template equivalent (manual setup)
- [Backstage Scaffolder docs](https://backstage.io/docs/features/software-templates/)
