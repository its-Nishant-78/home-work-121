def calculate_conditional_probability(total_balls, white_balls):
    return white_balls / total_balls

total_balls = 10
white_balls = 3
probability = calculate_conditional_probability(total_balls, white_balls)
print("Conditional probability:", probability)