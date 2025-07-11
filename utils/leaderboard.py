import heapq
import pandas as pd

def build_leaderboard(resume_data: list) -> pd.DataFrame:
    pq = []

    for entry in resume_data:
        name = entry["Name"]
        score = entry["Score"]
        feedback = entry["Feedback"]
        heapq.heappush(pq, (-score, name, feedback))

    leaderboard = []
    while pq:
        score_neg, name, feedback = heapq.heappop(pq)
        leaderboard.append({"Name": name, "Score": -score_neg, "Feedback": feedback})

    return pd.DataFrame(leaderboard)
