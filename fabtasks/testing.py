from fabric.api import task, local


@task
def pytest():
    """
    Run tests locally in the current environment.
    """
    local('py.test --cov sphinx_autobuild')
    local('coverage html')
