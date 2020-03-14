import nox
import toml

project_name = ""
with open("./pyproject.toml") as pyproj_toml:
    parsed_toml = toml.load(pyproj_toml)
    project_name = parsed_toml["tool"]["poetry"]["name"].replace("-", "_")

nox.options.stop_on_first_error = False
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["full"]


def deps(session):
    session.install("poetry")
    session.run("poetry", "install")


@nox.session()
def full(session):
    deps(session)
    session.run("black", ".")
    session.run("pytest", "-rap", "tests/")
    session.run(
        "coverage", "run", f"--source={project_name}", "-m", "pytest", "./tests/",
    )
    session.run("flake8", project_name)
    session.run("pylint", "--rcfile=./nox.ini", project_name)
    session.run("mypy", "--config-file=./nox.ini", project_name, "tests")
    session.run("bandit", "-r", "-v", project_name)
    session.run("coverage", "report", "--fail-under=80", "-m")
    session.run("poetry", "build", "-v")


@nox.session()
def black(session):
    deps(session)
    session.run("black", ".")


@nox.session()
def tests(session):
    deps(session)
    session.run("pytest", "-rap", "tests/")


@nox.session()
def coverage(session):
    deps(session)
    session.run(
        "coverage", "run", f"--source={project_name}", "-m", "pytest", "./tests/",
    )
    session.run("coverage", "report", "--fail-under=80", "-m")


@nox.session()
def flake8(session):
    deps(session)
    session.run("flake8", project_name)


@nox.session()
def pylint(session):
    deps(session)
    session.run("pylint", "--rcfile=./nox.ini", project_name)


@nox.session()
def mypy(session):
    deps(session)
    session.env["MYPYPATH"] = project_name
    session.run("mypy", "--config-file=./nox.ini", project_name, "tests")


@nox.session()
def bandit(session):
    deps(session)
    session.run("bandit", "-r", "-v", project_name)


@nox.session()
def build(session):
    deps(session)
    session.run("poetry", "build", "-v")
