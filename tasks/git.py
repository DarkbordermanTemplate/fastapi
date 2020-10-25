"""Git related tasks"""
from invoke import task

from .common import VENV_PREFIX


@task
def install_precommit(context):
    context.run(f"{VENV_PREFIX} pre-commit install")
