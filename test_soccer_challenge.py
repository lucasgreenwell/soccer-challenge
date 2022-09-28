from click.testing import CliRunner
from soccer_challenge import calculate_season


def test_calculate_season():
  runner = CliRunner()
  result = runner.invoke(calculate_season, ["./sample-input.txt"])
  expected_output = open("expected-output.txt", 'r').read()
  assert result.exit_code == 0
  assert result.output.strip().replace("\n", "") == expected_output.strip().replace("\n", "")

