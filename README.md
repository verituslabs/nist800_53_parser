# nist800_53_parser

This is an open source project to write a simple parser for the NIST 800.53 standard (https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final).

The object is to use existing JSON parsing libraries to ingest the JSON version of the standard and then provide a simple API to transform the standard.

## Prerequisites
1. Learn simple python
2. Learn PEP 08 -- https://pep8.org/
3. Learn Tying https://docs.python.org/3/library/typing.html
4. Use Black https://pypi.org/project/black/
5. Learn pytest https://docs.pytest.org/en/stable/index.html
6. Learn Pipenv https://pypi.org/project/pipenv/
7. Learn Basic Git and Github -- enough to clone a project, add, commit and send a pull request

## Workflow
1. Check out the project
2. Install Black and make sure you can run pytest
3. Use pipenv to initilaize the environment (basically go to the dir and say pipenv shell) if you get a shell you are in a good place
4. Write your code
5. Write your unit-tests -- you are done when all your unit tests pass
6. Propose new methods to the class -- implement those new methods
