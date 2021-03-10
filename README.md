# Balancy
Query balances for certain accounts and more on Ethereum.

**This project is under development! Get back later for more information.**
&nbsp;

## Project dependencies

#### With poetry:
Run `poetry install` in the project root folder.
#### With pip:
Run `pip install -r requirements.txt`.
&nbsp;

## Using the cli tool:
Inside the project root folder run `python balancy.py --help` for available commands.
For some functions you will have to pass in a web3 provider url and a database uri as flags.
If you have docker installed you can use `docker-compose up` to start an *etcd* database instance and a *ganache* as a web3 test node.
Example commands with docker-compse running:
```console
python balancy.py api --w3url http://127.0.0.1:8545 --db-uri http://127.0.0.1:2379
python balancy.py fetch-token --db-uri http://127.0.0.1:2379 --w3url http://127.0.0.1:8545
```
You want to fork a live node with ganache-cli using docker-compose, you can create a `.env` file and specify the node url inside it like this:
```
WEB3_FORK_URL=<YOUR URL HERE>
```

&nbsp;
## The web api:
You can run the web api with the cli command below:
```console
python balancy.py api -p 8000
```
After the web api started up you can check its available endpoints with the generated OpenAPI docs on this link: http://127.0.0.1:8000/docs#/ (if you are running it on localhost port 8000)

&nbsp;
## Packages and tools:
- https://typer.tiangolo.com/
- https://github.com/kragniz/python-etcd3
- https://web3py.readthedocs.io/en/stable/
- https://github.com/trufflesuite/ganache-cli
- https://python-poetry.org/
