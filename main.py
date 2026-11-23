
import matplotlib.pyplot as plt
import numpy as np
# завдання 1
months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec',
]
plan = [100, 120, 130, 150, 170, 160, 180, 200, 210, 220, 240, 250]
fact = [90, 110, 135, 140, 175, 155, 190, 195, 220, 215, 250, 260]


plt.figure(figsize=(10, 5))
plt.plot(
    months, plan, label='Plan (Ruahman)', marker='o', color='blue', linestyle='--'
)
plt.plot(
    months, fact, label='Fact (Thawk chhuah)', marker='s', color='green'
)

plt.xlabel('Thla (Months)')
plt.ylabel('Prog (Values)')
plt.title('Plan vs Fact Tawn tlangkhawmna Graph')


plt.legend()
plt.grid(True)


plt.show()


# завдання 2

np.random.seed(42)
ages = np.random.randint(18, 61, size=100)


plt.figure(figsize=(8, 5))
plt.hist(ages, bins=10, color='skyblue', edgecolor='black')

mean_age = np.mean(ages)
plt.axvline(
    mean_age,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'Average: {mean_age:.1f}',
)

plt.xlabel('Kum Zat (Age)')
plt.ylabel('Mi Zat (Frequency)')
plt.title('Mite Kum Zat Insemdarhna Histogram')

plt.legend()
plt.grid(True, alpha=0.3)

plt.show()

# завдання 3

np.random.seed(10)
group_a = np.random.normal(75, 10, 50)
group_b = np.random.normal(82, 8, 50)
group_c = np.random.normal(68, 12, 50)

plt.figure(figsize=(8, 5))
plt.boxplot([group_a, group_b, group_c], labels=['Group A', 'Group B', 'Group C'])

plt.xlabel('Zirlai Pawl (Groups)')
plt.ylabel('Mark / Result')
plt.title('Group 3 te Exam Result Boxplot Tehkhinna')

plt.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.show()
