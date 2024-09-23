import subprocess


def export_requirements():
    try:

        result = subprocess.check_output(["pip", "freeze"])


        with open("requirements.txt", "wb") as f:
            f.write(result)
        print("Requirements exported successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    export_requirements()