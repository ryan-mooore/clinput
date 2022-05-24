from invalid.prompt import _Prompt
import mock, builtins


def test_prompt(monkeypatch):
    prompt = _Prompt()
    with mock.patch.object(builtins, "input", lambda _: "test"):
        result = prompt.prompt("message")
        assert result == "test"
