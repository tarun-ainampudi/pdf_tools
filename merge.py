import argparse
from pypdf import PdfWriter, PdfReader

parser = argparse.ArgumentParser(description="Remove password from a PDF")
parser.add_argument("pdfs", help="Comma seperated pdf paths to merge")
parser.add_argument(
    "-o",
    "--output",
    type=str,
    required=False,
    default="merged_pdf.pdf",
    help="Output filename"
)

args = parser.parse_args()

def merge_pdfs(input_files: list[str], output_file: str) -> None:
    writer = PdfWriter()

    for pdf_path in input_files:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)
        print(f"Added {len(reader.pages)} page(s) from '{pdf_path}'")

    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"\nMerged PDF saved to: '{output_file}'")


pdf_files = args.pdfs.split(",")
merge_pdfs(pdf_files, args.output)