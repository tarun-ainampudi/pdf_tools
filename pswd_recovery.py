import pikepdf
import sys
import exrex
import time

pass_found = False
attempts = 0
start = time.perf_counter()


def check_password(file_path, password):
    global pass_found
    global attempts
    if pass_found:
        return
    try:
        with pikepdf.open(file_path, password=password):
            print(f"[✓] Password found: {password}")
            pass_found = True
    except pikepdf.PasswordError:
        pass
    except Exception as e:
        print(f"Uncaught Exception Occured: {e}")
    finally:
        attempts += 1


def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("    python pswd_recovery.py <path> <regex>")
        return

    pdf_path = sys.argv[1]
    pass_regex = sys.argv[2]

    global pass_found
    global attempts

    for match in exrex.generate(pass_regex):
        if pass_found:
            break
        check_password(pdf_path, match)
    now = time.perf_counter()
    spent = now - start
    if spent > 0:
        speed = attempts/spent
        print(f"speed: {speed} pass/sec")


if __name__ == "__main__":
    main()
