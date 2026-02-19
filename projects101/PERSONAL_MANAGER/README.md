1. Identity Engine
    Defines what a “strong day” is.
        Medical identity:
            - ≥ 2 topic
            - ≥ 2 hour revision

        Tech identity:
            - ≥ 1 commit
            - ≥ 30 min coding

        Health identity:
            - Exercise done
            - Junk food = 0

        Learning identity:
            - History OR Finance learned
            - ≥ 10 pages book OR podcast insight logged

                This engine determines:
                    ID Score
                    Identity alignment %
                    Weakest identity category
2. Scoring Engine
    Every day generates:
    Discipline score
    Focus score
    Financial score
    Health score
    Learning score
        Then produces: Overall ID Score = weighted average

3. Finance Engine
    Daily log:
        {
            "date": "2026-02-17",
            "transactions": [
                {
                    "type": "expense",
                    "category": "food",
                    "amount": 300,
                    "transaction_cost": 5
                }]
        }

    Metrics generated:
        Daily net
        Expense ratio
        Junk-food spending rate
        Transaction cost leakage
        Monthly burn rate
        Savings rate

4. Streak Engine       
    Tracks:
        Coding streak
        Exercise streak
        No-junk streak
        Learning streak
        Income generation streak

5. Study Log System
    Tracks:
            {
        "domain": "medicine",
        "topic": "cold chain management",
        "time_spent": 45,
        "retention_score": 7/10,
        "revision_due": "2026-02-20"
            }

6. Daily Workflow (How You’ll Use It)
    Each day:
        Run main.py
        Input:
            Coding minutes
            Topics studied
            Exercise
            Junk food?
            Book pages
            Podcast insight
            History/Finance topic
            Transactions
        System calculates:
            Scores
            Identity alignment
            Streaks
            Financial net
        Generates a blunt daily feedback report.

7. Long-Term Evolution Plan

    Phase 1 (Month 1):
        CLI-based
        JSON storage
        Basic scoring
    Phase 2:
        Add data visualization
        Trend graphs
        Weekly analysis
    Phase 3:
        Add prediction engine
        Burnout detection
        Budget forecasting
    Phase 4:
        Add recommendation system
        “Based on your past 30 days…”