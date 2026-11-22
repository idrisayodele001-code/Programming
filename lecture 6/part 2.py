people_data = open("group.txt").readlines()

people = [person.split() for person in people_data]

# TASK 1
female_rasa = [person for person in people if person[1] == "Rasa" and person[3] == "female"]

print(f"{len(female_rasa)} female whose name is Rasa")

# TASK 2
smokers = [person for person in people if person[8] == "yes"]

smoke_more_than_10_years = [person for person in people if int(person[9]) >= 10]

male_smokers = [person for person in smoke_more_than_10_years if person[3] == "male"]
female_smokers = [person for person in smoke_more_than_10_years if person[3] == "female"]

percentage_of_smokers = float(len(smokers) / len(people) * 100)
percentage_of_smokers_more_than_10_years = float(len(smoke_more_than_10_years) / len(smokers) * 100)
male_percentage_of_smokers_more_than_10_years = float(len(male_smokers) / len(smoke_more_than_10_years) * 100)
female_percentage_of_smokers_more_than_10_years = float(len(female_smokers) / len(smoke_more_than_10_years) * 100)

print(f"{percentage_of_smokers}% of people smoke and ({percentage_of_smokers_more_than_10_years}% of smokers): {len(smoke_more_than_10_years)} people smoke more than 10 years and {male_percentage_of_smokers_more_than_10_years}% of them is male and {female_percentage_of_smokers_more_than_10_years}% of them is female")

non_smokers = [person for person in people if person[8] == "no"]

male_non_smokers = [person for person in non_smokers if person[3] == "male"]
female_non_smokers = [person for person in non_smokers if person[3] == "female"]

percentage_of_non_smokers = float(len(non_smokers) / len(people) * 100)
percentage_of_male_non_smokers = float(len(male_non_smokers) / len(people) * 100)
percentage_of_female_non_smokers = float(len(female_non_smokers) / len(people) * 100)

print(f"{percentage_of_non_smokers}% people do not smoke, {percentage_of_female_non_smokers}% of them is female and {percentage_of_male_non_smokers}% of them is male")

# TASK 3
ages_of_male = [2026 - int(person[5]) for person in people if person[3] == "male"]
ages_of_female = [2026 - int(person[5]) for person in people if person[3] == "female"]

avg_male_age = int(sum(ages_of_male) / len(ages_of_male))
avg_female_age = int(sum(ages_of_female) / len(ages_of_female))

print(f"Average age for men is {avg_male_age} and for women is {avg_female_age}")

# TASK 4
people_with_children = [person for person in people if int(person[-1]) > 0]

print(f"{len(people_with_children)} people have children")

# TASK 5
first_filter = open("first_filter.txt", "w")

first_filter.write("Surname\tName\tCity\tPhone Number\n")

blue_eyed_non_smokers_no_children_under_age_23_normal_weight = [[person[0], person[1], person[2], person[4]] for person in people if person[7] == "blue" and person[8] == "no" and person[10] == "0" and 2026 - int(person[4]) < 23 and 56 <= int(person[6]) <= 68]

for person in blue_eyed_non_smokers_no_children_under_age_23_normal_weight:
    for data in person:
        first_filter.write(f"{data}\t")
    first_filter.write("\n")

# TASK 6
second_filter = open("second_filter.txt", "w")

second_filter.write("Surname\tName\tCity\tEye Color\tSmoking\tPhone Number\n")

male_more_than_1_child_over_90_kg_over_50_years = [[person[0], person[1], person[2], person[7], person[8], person[4]] for person in people if person[3] == "male" and int(person[-1]) > 1 and int(person[6]) > 90 and 2026 - int(person[4]) > 50]

for person in male_more_than_1_child_over_90_kg_over_50_years:
    for data in person:
        second_filter.write(f"{data}\t")
    second_filter.write("\n")
