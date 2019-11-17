# How to run the project?
* open terminal, go to project root directory and execute
```bash
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
pytest --cov=shoppingcart --cov=models --cov=data --cov-report=html
```
* To view the coverage report, we can run
```bash
firefox htmlcov/index.html
```
* This project works with `Python 3.7.3`
* The sqlite file `database.db` is included in the project. In case we want to recreate the file, run the following commands in project root directory
```bash
export PYTHONPATH=.
alembic upgrade head
```
* For any questions, you can message me on `ambhore.pranav@gmail.com`
