import random

def simulate_point(prob_a):
    """模拟1分的争夺，prob_a是A选手得分的概率"""
    return random.random() < prob_a

def simulate_game(prob_a):
    """模拟1局比赛（乒乓球11分制，需净胜2分）"""
    score_a, score_b = 0, 0
    while True:
        if simulate_point(prob_a):
            score_a += 1
        else:
            score_b += 1
        
        # 满足11分且净胜2分则结束
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 1 if score_a > score_b else 0

def simulate_match(prob_a, best_of=3):
    """模拟1场比赛（3局2胜制）"""
    wins_a, wins_b = 0, 0
    for _ in range(best_of):
        if simulate_game(prob_a):
            wins_a += 1
        else:
            wins_b += 1
        # 先赢2局则结束
        if wins_a == (best_of + 1) // 2 or wins_b == (best_of + 1) // 2:
            break
    return 1 if wins_a > wins_b else 0

def analyze_competition(prob_a, num_matches):
    """分析竞技规律：统计num_matches场比赛中A选手的胜率"""
    wins_a = 0
    for _ in range(num_matches):
        wins_a += simulate_match(prob_a)
    win_rate = wins_a / num_matches
    print(f"A选手得分概率：{prob_a:.2f}")
    print(f"模拟{num_matches}场比赛后，A选手胜率：{win_rate:.2%}")
    return win_rate

# 示例：A选手得分概率为0.55，模拟1000场比赛
if __name__ == "__main__":
    analyze_competition(prob_a=0.55, num_matches=1000)
