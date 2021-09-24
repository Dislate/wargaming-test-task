from test_task import app
from test_task.commands import start_cli

app.cli.add_command(start_cli)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
