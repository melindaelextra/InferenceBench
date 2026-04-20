"""Application entrypoint."""

from app.api.routes import router


def main() -> None:
    """Run a basic startup check."""
    print("Inference Bench app is set up.")
    print(f"Loaded router: {router}")


if __name__ == "__main__":
    main()
