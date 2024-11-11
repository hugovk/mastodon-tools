"""
Get credentials for the Mastodon API with Mastodon.py

Based on this gist by Allison Parrish
https://gist.github.com/aparrish/661fca5ce7b4882a8c6823db12d42d26
"""
import argparse

from mastodon import Mastodon  # pip install Mastodon.py


def mastodon_create_app(
    app_name: str, email: str, password: str, instance: str
) -> None:
    client_id, client_secret = Mastodon.create_app(
        app_name, scopes=["read", "write"], api_base_url=instance
    )

    print(f"mastodon_client_id: {client_id}")
    print(f"mastodon_client_secret: {client_secret}")

    api = Mastodon(client_id, client_secret, api_base_url=instance)
    access_token = api.log_in(email, password, scopes=["read", "write"])

    print(f"mastodon_access_token: {access_token}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Get credentials for the Mastodon API with Mastodon.py",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("app_name", help="Your app name")
    parser.add_argument("email", help="Email you used to create your bot's account")
    parser.add_argument(
        "password", help="Password you used to create your bot's account"
    )
    parser.add_argument(
        "--instance", default="https://mas.to", help="Mastodon instance"
    )
    args = parser.parse_args()
    mastodon_create_app(args.app_name, args.email, args.password, args.instance)


if __name__ == "__main__":
    main()
