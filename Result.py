subjects =int(input("How Many Subjects? "))
def calculate_average(scores):
    total = sum(scores)
    return total / len(scores)

def main():
    # create an empty list to store the scores
    scores = []
    for i in range(1, subjects+1):
        try:
          score = float(input(f"Enter score for subject {i}: "))
          scores.append(score)
        except:
            print("Invalid input. Please enter a valid numerical score.")
        
    # Calculate and display the average score
    average = calculate_average(scores)
    print(f"The average score is: {average:.2f}")

if __name__ == "__main__":
    main()

