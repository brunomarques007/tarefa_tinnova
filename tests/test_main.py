from typer.testing import CliRunner

from main import (
    app,
)

runner = CliRunner()


def test_task_1_output():
    result = runner.invoke(app, ['task-1'])
    assert result.exit_code == 0

    assert (
        '\x1b[1;32mPercentage of valid votes: \x1b[0m'
        '\x1b[1;36m80.00\x1b[0m'
        '\x1b[1;32m%\x1b[0m\n'
    ) in result.stdout

    assert (
        '\x1b[1;33mPercentage of white votes: \x1b[0m'
        '\x1b[1;36m15.00\x1b[0m'
        '\x1b[1;33m%\x1b[0m\n'
    ) in result.stdout

    assert (
        '\x1b[1;31mPercentage of null votes: \x1b[0m'
        '\x1b[1;36m5.00\x1b[0m'
        '\x1b[1;31m%\x1b[0m\n'
    ) in result.stdout


def test_task_2_output():
    result = runner.invoke(app, ['task-2'])
    assert result.exit_code == 0

    assert (
        '\x1b[1;32mSorted Array: \x1b[0m'
        '\x1b[1;32m[\x1b[0m'
        '\x1b[1;36m0\x1b[0m\x1b[1;32m, \x1b[0m'
        '\x1b[1;36m1\x1b[0m\x1b[1;32m, \x1b[0m'
        '\x1b[1;36m2\x1b[0m\x1b[1;32m, \x1b[0m'
        '\x1b[1;36m3\x1b[0m\x1b[1;32m, \x1b[0m'
        '\x1b[1;36m4\x1b[0m\x1b[1;32m, \x1b[0m'
        '\x1b[1;36m5\x1b[0m\x1b[1;32m, \x1b[0m'
        '\x1b[1;36m6\x1b[0m\x1b[1;32m, \x1b[0m'
        '\x1b[1;36m7\x1b[0m\x1b[1;32m]\x1b[0m\n'
    ) in result.stdout


def test_task_3_output():
    result = runner.invoke(app, ['task-3'])
    assert result.exit_code == 0

    assert (
        '\x1b[1;35mThe factorial of \x1b[0m'
        '\x1b[1;36m5\x1b[0m'
        '\x1b[1;35m is \x1b[0m'
        '\x1b[1;36m120\x1b[0m\n'
    ) in result.stdout


def test_task_4_output():
    result = runner.invoke(app, ["task-4"])
    assert result.exit_code == 0

    assert (
        "\x1b[1;34mThe sum of multiples of \x1b[0m"
        "\x1b[1;34m[\x1b[0m"
        "\x1b[1;36m3\x1b[0m"
        "\x1b[1;34m, \x1b[0m"
        "\x1b[1;36m5\x1b[0m"
        "\x1b[1;34m]\x1b[0m"
        "\x1b[1;34m bellow \x1b[0m"
        "\x1b[1;36m10\x1b[0m"
        "\x1b[1;34m is \x1b[0m"
        "\x1b[1;36m23\x1b[0m\n"
    ) in result.stdout
