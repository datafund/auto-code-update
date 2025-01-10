import os
import argparse
import difflib

def is_text_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            # Read a small portion of the file to check for text content
            chunk = f.read(1024)
            chunk.decode('utf-8')
        return True
    except (UnicodeDecodeError, IOError):
        return False

def get_txt_files_recursively(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_text_file(file_path):
                yield file_path


def merge_file(original_file, modified_file, output_file):
    """
    Merges `modified_file` into `original_file` by applying only new and changed lines, ignoring deletions.
    The result is saved to `output_file`.
    """
    with open(original_file, 'r') as orig:
        original_lines = orig.readlines()
    with open(modified_file, 'r') as updated:
        updated_lines = updated.readlines()
    
    # Use SequenceMatcher to find changes
    diff = difflib.SequenceMatcher(None, original_lines, updated_lines)
    
    merged_lines = []
    for tag, i1, i2, j1, j2 in diff.get_opcodes():
        if tag == 'replace' or tag == 'insert':
            # Add new or modified lines from updated file
            merged_lines.extend(updated_lines[j1:j2])
        elif tag == 'equal':
            # Keep lines that are unchanged
            merged_lines.extend(original_lines[i1:i2])
        elif tag == 'delete':
            # Include deleted lines from original file
            merged_lines.extend(original_lines[i1:i2])
    
    # Write the merged content to the output file
    with open(output_file, 'w') as output:
        output.writelines(merged_lines)

    print(f"Merged file saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Recursively read all text files in a folder.")
    parser.add_argument('source', type=str, help="Path to the folder to read")
    parser.add_argument('dest', type=str, help="Path to the repo to patch")
    
    args = parser.parse_args()
    source_path = args.source
    repo_path = args.dest
    
    if os.path.isdir(source_path):
        for file_path in get_txt_files_recursively(source_path):
            relative_path = os.path.relpath(file_path, source_path)
            dest_file = os.path.join(repo_path, relative_path)
            merge_file(dest_file, file_path, dest_file)
    else:
        print(f"The provided path is not a valid directory: {source_path}")

if __name__ == "__main__":
    main()
