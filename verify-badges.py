import sys
import textwrap
import requests

EXPECTED_BADGE_LINE_NUMBER = 3

def main():
    response = requests.get("https://api.github.com/orgs/build-and-test/repos")
    response.raise_for_status()
    repos = response.json()
    for repo in [r for r in repos if not r["archived"] and r["name"] != ".github"]:
        repo_name = repo["name"]
        readme_url = f"https://raw.githubusercontent.com/build-and-test/{repo_name}/master/README.md"
        print("Checking", readme_url)
        response = requests.get(readme_url)
        response.raise_for_status()
        readme = response.text
        badge_line = readme.splitlines()[EXPECTED_BADGE_LINE_NUMBER - 1]
        
        expected = f"[![Build and Test](https://github.com/build-and-test/{repo_name}/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/build-and-test/{repo_name}/actions/workflows/build-and-test.yml?query=branch%3Amain)"
        if badge_line != expected:
            sys.exit(textwrap.dedent(f"""\
                Incorrect Build-and-Test badge on line {EXPECTED_BADGE_LINE_NUMBER}",
                    Expected on line {EXPECTED_BADGE_LINE_NUMBER}: {expected}
                    Actual: {badge_line}
                    -----------------------
                    {readme}
                """))


if __name__ == "__main__":
    main()
