import pytest

from django_custom_commands.management import call_command, execute_from_command_line, get_commands


@pytest.fixture(autouse=True)
def clear_cache():
    get_commands.cache_clear()


def test_call_command_default():
    assert call_command("custom_command") == "app-command"


def test_get_commands_default():
    assert get_commands()["custom_command"] == "test_project.app"


def test_execute_from_command_line_default(capsys):
    execute_from_command_line(["manage.py", "custom_command"])
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out.strip() == "app-command"


def test_call_command_custom_locations(settings):
    settings.CUSTOM_COMMAND_LOCATIONS = ["test_project.custom"]
    assert call_command("custom_command") == "custom-command"


def test_get_commands_custom_locations(settings):
    settings.CUSTOM_COMMAND_LOCATIONS = ["test_project.custom"]
    assert get_commands()["custom_command"] == "test_project.custom"


def test_execute_from_command_line_custom_locations(settings, capsys):
    settings.CUSTOM_COMMAND_LOCATIONS = ["test_project.custom"]
    execute_from_command_line(["manage.py", "custom_command"])
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out.strip() == "custom-command"
