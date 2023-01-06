## How to use the code in this repository. 

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

4 Execute code.

```
python ./scripts curlapi.py