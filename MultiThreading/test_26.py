# Barrier Object

# import threading
# import time

# def player(name):
#     print(f"{name} started")
#     score = 0

#     for i in range(5):
#         time.sleep(3)
#         print(f"{name} is playing")

#         print(f"{name} scored {score}")
#         print(f"sending winning amount to {name}")

# Threads = []

# players_names = ["Souvik", "Soukarjya", "Dipankar", "Moni"]
# for name in players_names:
#     thread = threading.Thread(target=player, args=(name,))
#     Threads.append(thread)
#     thread.start()


print("\n###############################\n")

# import threading
# import time

# number_of_players = 4
# barrier = threading.Barrier(number_of_players)

# def player(name):
#     print(f"{name} started")
#     score = 0

#     for i in range(5):
#         time.sleep(3)
#         print(f"{name} is playing")

#         barrier.wait()

#         print(f"{name} scored {score}")
#         print(f"sending winning amount to {name}")

# Threads = []

# players_names = ["Souvik", "Soukarjya", "Dipankar", "Moni"]
# for name in players_names:
#     thread = threading.Thread(target=player, args=(name,))
#     Threads.append(thread)
#     thread.start()

print("\n###############################\n")

import threading
import time

number_of_players = 4
barrier = threading.Barrier(number_of_players)
print_lock = threading.Lock()  # For ordered print

rounds = 5
players_names = ["Souvik", "Soukarjya", "Dipankar", "Moni"]

# Shared list to collect messages for ordered printing
results_by_round = [[] for _ in range(rounds)]

def player(index, name):
    score = 0
    for i in range(rounds):
        time.sleep(1 + index)  # Staggered time to simulate different pace
        message = (
            f"{name} is playing\n"
            f"{name} scored {score}\n"
            f"sending winning amount to {name}"
        )

        # Store message in the round bucket
        results_by_round[i].append((index, message))

        barrier.wait()  # Synchronize all players before printing

        # Only one thread prints per round, in order
        if index == 0:
            with print_lock:
                print(f"\n--- Round {i + 1} Results ---")
                for _, msg in sorted(results_by_round[i]):
                    print(msg)
                print("--------------------------\n")
            barrier.wait()  # Ensure all threads wait until print is done
        else:
            barrier.wait()

threads = []
for idx, name in enumerate(players_names):
    t = threading.Thread(target=player, args=(idx, name))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
