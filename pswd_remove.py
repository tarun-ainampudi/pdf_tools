import argparse
import os
import shutil
import pikepdf

parser = argparse.ArgumentParser(description="Remove password from a PDF")

parser.add_argument("pdf", help="Path to the PDF")
parser.add_argument("password", help="PDF password")
parser.add_argument(
    "-r",
    "--replace",
    action="store_true",
    help="Replace the original file"
)

args = parser.parse_args()

try:
    with pikepdf.open(args.pdf, password=args.password) as pdf:
        if args.replace:
            output = args.pdf + ".tmp"
            pdf.save(output)
            shutil.move(output, args.pdf)
        else:
            base, ext = os.path.splitext(args.pdf)
            output = f"{base}_nopswd{ext}"
            pdf.save(output)

    print(f"[✓] Saved: {output}")

except pikepdf.PasswordError:
    print("[!] Incorrect password.")
except FileNotFoundError:
    print("[!] PDF file not found.")
except Exception as e:
    print(f"[!] Error: {e}")