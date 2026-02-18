import nox


def _run_tests(session: nox.Session, numpy_spec: str) -> None:
    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install(numpy_spec)
    session.install(".[test]")
    session.run("pytest", "-q")


@nox.session(python="3.11")
def tests_py311_np1(session: nox.Session) -> None:
    _run_tests(session, "numpy<2")


@nox.session(python="3.11")
def tests_py311_np2(session: nox.Session) -> None:
    _run_tests(session, "numpy>=2,<3")


@nox.session(python="3.13")
def tests_py313_np2(session: nox.Session) -> None:
    _run_tests(session, "numpy>=2,<3")
