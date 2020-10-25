"""Code related tasks"""
from invoke import task

from .common import VENV_PREFIX


@task
def pylint(context):
    context.run(f"{VENV_PREFIX} pylint --rcfile=setup.cfg api/**")


@task
def flake8(context):
    context.run(f"{VENV_PREFIX} flake8 api --max-line-length=120")


@task
def mypy(context):
    context.run(f"{VENV_PREFIX} mypy api")


@task
def bandit(context):
    context.run(f"{VENV_PREFIX} bandit api")


@task(pre=[pylint, flake8, mypy, bandit])
def lint(context):
    pass


@task
def black(context):
    context.run(f"{VENV_PREFIX} black api")


@task
def isort(context):
    context.run(f"{VENV_PREFIX} isort api")


@task(pre=[black, isort])
def reformat(context):
    pass


@task
def pytest(context):
    context.run(f"{VENV_PREFIX} pytest -vv --cov-report=term-missing --cov=api/endpoints api/tests")


@task(pre=[reformat, lint, pytest])
def bundle(context):
    pass
