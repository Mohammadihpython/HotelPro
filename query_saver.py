import subprocess


def make_sql_query(
    app_name: str,
    migration_number: str,
):
    command = f"python manage.py sqlmigrate {app_name} {migration_number}"
    output = subprocess.check_output(command, shell=True, encoding="utf-8")

    with open(f"./sql_queries/{app_name}-{migration_number}.sql", "w+") as f:
        f.write(output)


make_sql_query("account", "0001_initial")
