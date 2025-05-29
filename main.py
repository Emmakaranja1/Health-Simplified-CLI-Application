import typer
from db.database import get_db
from controllers import users
from sqlalchemy.orm import Session

app = typer.Typer(help="Manage your users via CLI")

@app.command("list-users")
def list_users():
    """
    List all users in Health Simplified.
    """
    db: Session = next(get_db())
    all_users = users.list_users(db)

    if all_users:
        typer.echo("📋 List of users:")
        for user in all_users:
            typer.echo(f"- ID: {user.id}, Name: {user.name}")
    else:
        typer.echo("❗ No users found.")

# This must come after all @app.command() declarations
if __name__ == "__main__":
    app()

