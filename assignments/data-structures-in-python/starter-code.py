"""Starter code for Data Structures in Python assignment."""


def task_one_examples():
    # TODO 1: Create and modify a list with at least 5 items.
    items = []

    # TODO 2: Create a dictionary with at least 3 key-value pairs.
    student_scores = {}

    # TODO 3: Create a set that starts with duplicate values.
    unique_names = set()

    # TODO 4: Create a tuple with fixed metadata.
    assignment_info = ()

    print("List example:", items)
    print("Dictionary example:", student_scores)
    print("Set example:", unique_names)
    print("Tuple example:", assignment_info)


def task_two_challenge():
    signups = ["Ava", "Noah", "Ava", "Mia", "Noah", "Leo"]

    # TODO 1: Convert signups into a unique participant set.
    participants = set()

    # TODO 2: Create a dictionary mapping each participant to an activity.
    activity_map = {}

    # TODO 3: Store fixed challenge details in a tuple.
    challenge_meta = ()

    print("Total sign-ups:", len(signups))
    print("Unique participants:", len(participants))
    print("Activity assignments:", activity_map)
    print("Challenge metadata:", challenge_meta)


if __name__ == "__main__":
    task_one_examples()
    print("-" * 40)
    task_two_challenge()
