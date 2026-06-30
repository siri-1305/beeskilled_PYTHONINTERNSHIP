def export_high_salary(df):
    """
    Export employees earning above 100000.
    """

    high_salary = df[df["Salary"] > 100000]

    high_salary.to_csv(
        "reports/high_salary_employees.csv",
        index=False
    )

    print("High salary employees exported successfully.")

def export_department_summary(df):

    summary = (
        df.groupby("Department")
        .agg(
            Employee_Count=("Department", "count"),
            Average_Salary=("Salary", "mean")
        )
    )

    summary.to_csv(
        "reports/department_summary.csv"
    )

    print("Department summary exported successfully.")
def export_summary(df):

    with open(
        "reports/summary.txt",
        "w"
    ) as file:

        file.write("EMPLOYEE ANALYSIS REPORT\n")
        file.write("=========================\n\n")

        file.write(
            f"Total Employees : {len(df)}\n"
        )

        file.write(
            f"Average Salary : {df['Salary'].mean():.2f}\n"
        )

        file.write(
            f"Highest Salary : {df['Salary'].max()}\n"
        )

        file.write(
            f"Lowest Salary : {df['Salary'].min()}\n"
        )

    print("Summary report generated.")
