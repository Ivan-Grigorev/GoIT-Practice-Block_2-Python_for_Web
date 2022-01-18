from pylint.lint import Run
from pylint.reporters import text


with open("report.out", "w") as f:
    reporter = text.TextReporter(f)
    Run(["../formatting/example.py"], reporter=reporter, do_exit=False)
