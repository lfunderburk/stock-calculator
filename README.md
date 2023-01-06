## How to use the code in this repository. 

Ensure that you have a subscription (free is enough) to the following two services:

1. https://exchangeratesapi.io/

2. https://rapidapi.com/alphavantage/api/alpha-vantage

0. Clone the repository.

```
git clone https://github.com/lfunderburk/stock-calculator.git
cd stock-calculator/
```

1. Set up a virtual environment. This project assumes

```
conda create --name stock-api-venv python==3.10
```

2. Activate environment.

```
conda activate stock-api-venv
```

3. Install dependencies.

```
pip install -r requirements.txt
```

5. Create a .env file and store your API keys. 

For the project to work, you must have the following two entries:

```
XRapidAPIKey = my_key1
apilayerKey = my_key2
```
6. Execute

```
python ./scripts curlapi.py
```