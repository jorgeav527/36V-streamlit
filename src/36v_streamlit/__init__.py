def main() -> None:
    """Lanza el dashboard de Streamlit."""
    import sys
    from pathlib import Path

    from streamlit.web import cli as stcli

    sys.argv = ["streamlit", "run", str(Path(__file__).parent / "main.py")]
    sys.exit(stcli.main())
