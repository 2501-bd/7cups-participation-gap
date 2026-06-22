# 7 Cups – Participation Gap Study

Exploratory analysis for a research onboarding task.

I was exploring the 7 Cups platform and noticed that some support topics had hundreds of questions while others had none at all. This small project tries to understand that gap.

## What's here

- `data.csv` – 44 topics collected manually from the 7 Cups Q&A section (topic name, question count, category)
- `analysis.py` – loads the CSV, prints basic stats, and generates two charts
- `charts/` – output charts from the script (3 images)

## How to run

```
pip install pandas matplotlib
python analysis.py
```

## What I found

- 5 topics have zero questions (Cancer, Men's Issues, Adoption/Foster Care, Perinatal Mood Disorder, Racial & Cultural Identity)
- Mental Health topics dominate, but not evenly — some well-known conditions have very little activity
- Mean questions per active topic: ~298; maximum (Depression): 844

## What I'd do next

- Automate scraping with BeautifulSoup to get response counts and post text
- Try sentiment analysis on posts to see if tone differs by topic
- Model topic relationships as a graph (users who post in multiple topics = shared edge)
