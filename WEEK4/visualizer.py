import matplotlib.pyplot as plt

def plot_department_count(df):
	department_count = df["Department"].value_counts()
	department_count.plot(kind = "bar")

	plt.title("Employess by department")
	plt.xlabel("department")
	plt.ylabel("number of employees")
	plt.tight_layout()
	plt.savefig("charts/department_count.png")
	plt.show()


def plot_salary_distribution(df):

    plt.figure(figsize=(8,5))

    plt.hist(df["Salary"], bins=5)

    plt.title("Salary Distribution")

    plt.xlabel("Salary")

    plt.ylabel("Employees")

    plt.tight_layout()

    plt.savefig("charts/salary_distribution.png")

    plt.show()
