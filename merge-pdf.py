import PyPDF2

def merge_pdfs(file1, file2, output):
    pdf_merger = PyPDF2.PdfMerger()
    pdf_merger.append(file1)
    pdf_merger.append(file2)
    with open(output, 'wb') as output_pdf_file:
        pdf_merger.write(output_pdf_file)

def ensure_pdf_extension(file_name):
    if not file_name.endswith('.pdf'):
        return file_name + '.pdf'
    return file_name

def main():
    print("Enter the names of the files to be merged and the output file name.")
    file1_name = ensure_pdf_extension(input("File 1 name: "))
    file2_name = ensure_pdf_extension(input("File 2 name: "))
    output_name = ensure_pdf_extension(input("Merged file name: "))

    try:
        merge_pdfs(file1_name, file2_name, output_name)
        print(f"Files were merged into {output_name} successfully.")
    except FileNotFoundError:
        print("Error: One or more files were not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    input("Press enter to close.")

if __name__ == "__main__":
    main()