"""Environmental tasks"""
from invoke import task


@task
def clean(context):
    context.run("find . -type f -name '*.py[co]' -delete")
    context.run("find . -type d -name '__pycache__' -delete")
    context.run("rm -rf dist")
    context.run("rm -rf build")
    context.run("rm -rf *.egg-info")
    context.run("rm -rf .hypothesis")
    context.run("rm -rf .pytest_cache")
    context.run("rm -rf .tox")
    context.run("rm -f report.xml")
    context.run("rm -f coverage.xml")
    context.run("rm -f .coverage")
    context.run("rm -rf .mypy_cache")
