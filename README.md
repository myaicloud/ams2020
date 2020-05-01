# ams2020

## install
```bash
sudo apt install python3 python3-venv
```

## run a assignment
```bash
python3 -m venv ams2020-env
source ams2020-env/bin/activate
pip3 install wheel
pip3 install numpy scipy matplotlib plotly cvxpy
source ams2020-env/bin/activate

# e.g. run assignment1
python3 assignment1
```

## close virtual environment
```bash
deactivate
```
