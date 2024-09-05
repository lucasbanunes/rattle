from pypdf import PdfWriter, PdfReader
import argparse

parser = argparse.ArgumentParser(description='change page order of pdf')
parser.add_argument('--input', required=True,
                    type=str, help='input pdf file')
parser.add_argument('--output', required=True,
                    type=str, help='output pdf file')
parser.add_argument('--pages', default=None,
                    nargs='+', type=int, help='pages to be extracted')
args = parser.parse_args()

output_pdf = PdfWriter()
with open(args.input, 'rb') as readfile:
    input_pdf = PdfReader(readfile)
    if args.pages is None:
        pages = range(input_pdf.get_num_pages())
    else:
        pages = args.pages
    for page in pages:
        output_pdf.add_page(input_pdf.get_page(page))
    with open(args.output, "wb") as writefile:
        output_pdf.write(writefile)
