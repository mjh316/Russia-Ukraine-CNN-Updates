# This is a basic workflow to help you get started with Actions

name: scrape news

# Controls when the workflow will run
on:
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
  schedule:
    - cron: '0,15,30,45 12-23 * * *'
    

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  scrape:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2.4.0
      
      - name: Install dependencies
        run: pip install -r requirements.txt
        
      - name: Fetch latest data
        run: python main.py
      
      - name: Commit data
        run: |-
          if [[ `git status --porcelain` ]]; then
            git config user.name github-actions
            git config user.email github-actions@github.com
            git add -A
            git commit -m "add latest data"
            git push
          fi
