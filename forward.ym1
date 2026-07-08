.github/workflows/forward.yml
name: Forward Cards

on:
  schedule:
    - cron: '*/10 * * * *'
  workflow_dispatch:

jobs:
  forward:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        pip install telethon
    
    - name: Run script
      env:
        SESSION_STRING: ${{ secrets.SESSION_STRING }}
      run: |
        python forward.py
