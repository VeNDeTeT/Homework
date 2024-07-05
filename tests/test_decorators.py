from src.decorators import my_function


def test_console_log(capsys):
    my_function(10, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"