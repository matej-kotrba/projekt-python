# Animal quiz

user_answers = []

right_answers = []


def print_question(question, array_with_answers, right_answer):
    print(question)
    array_with_answers.append(right_answer)
    return input("Your answer: ")


def conclude_results(user_answers, right_answers):
    answer_array = []
    all_right_rumber = 0
    for i in range(len(user_answers)):
        if str(user_answers[i]).lower() == str(right_answers[i]).lower():
            answer_array.append(True)
            all_right_rumber += 1
        else:
            answer_array.append(False)
    return (all_right_rumber, answer_array)


user_answers.append(print_question("Which animal is characterised by ear flaps,"
                                   " short and thick hair and big chest and belly ?",
                                   right_answers, "Sea Lion"))

user_answers.append(print_question("Which pinniped is the most widespread one over world ?"
                                   " On surface moves by crawling on his belly.",
                                   right_answers, "Seal"))

user_answers.append(print_question("Which animal is large marine mammal ?",
                                   right_answers, "Walrus"))

results_number, results_array = conclude_results(user_answers, right_answers)

for i in range(len(results_array)):
    print(f"Question one: {'correct' if results_array[i] else 'incorrect'}")
print(f"Your total correct answer was {results_number} / {len(right_answers)}.")
