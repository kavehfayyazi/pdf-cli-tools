# pdfwiz

A lightweight CLI utility for manipulating PDFs.

## Features

- Merge two PDFs

- Rotate selected pages

- Reverse page order

- Delete pages

- Operate on specific pages or ranges

- In-place or save as new file

- Simple and intuitive CLI with helpful options

## Installation

```bash
git clone https://github.com/kavehfayyazi/pdfwiz.git
cd pdfwiz
pip install --user .
```

If `pdfwiz` is not found after install, make sure the appropriate scripts folder is in your `PATH`:

- macOS/Linux: `~/.local/bin`

- Windows: `%APPDATA%\Python\Scripts`

See [Troubleshooting](#troubleshooting) below for more details.

## Updating & Uninstalling

### Update to the latest version

```bash
cd pdfwiz
git pull origin main
pip install --user .
```

### Uninstall

```bash
pip uninstall pdfwiz
```

## Usage

```bash 
pdfwiz <command> [options]
```

### Available commands:

| Command | Description |
| :--- | :---: |
| `merge` | Merge two PDFs |
| `rotate` | Rotate pages |
| `reverse` | Reverse page order |
| `delete` | Delete selected pages |

### Example:

```bash
pdfwiz merge file1.pdf file2.pdf -o merged.pdf
pdfwiz rotate file.pdf -p 1:3 -a 90 -o rotated.pdf
```

Run:

```bash
pdfwiz --help
pdfwiz <command> --help
```

for full options.

## Specifying Pages and Ranges

Many commands in `pdfwiz` allow you to operate on specific pages or ranges of pages in a PDF.

You can specify pages using:

- Individual page numbers (1-based, e.g. `1,3,5`)

- Ranges using a colon (e.g. `2:4` for pages 2, 3, and 4)

- Combinations of both

### Examples

| Input | Expanded Pages |
| :--- | :---: |
| `all` | All pages in the document (default) |
| `1,3,5` | Pages 1, 3, and 5 |
| `2:4` | Pages 2, 3, and 4 |
| `1,3:5,7` | Pages 1, 3, 4, 5, and 7 |

## Contributing

1. **Fork** this repository.

2. **Clone** your fork locally:

    ```bash
    git clone https://github.com/<your-username>/pdfwiz.git
    cd pdfwiz
    ```

3. **Create** a new branch:

    ```bash
    git checkout -b feature/your-feature
    ```

4. **Commit** your changes:

    ```bash
    git commit -m "Add feature-name."
    ```

5. **Push** to the branch

    ```bash
    git push origin feature/feature-name
    ```

6. **Open** a pull request.

## Troubleshooting

**Command not found?**

Your Python "scripts" folder may not be in your PATH.

- **macOS/Linux**:

    Add to your shell config (`~/.bashrc` or `~/.zshrc`):

    ```bash
    export PATH="$HOME/.local/bin:$PATH"
    ```
- **Windows**:

    Add `%APPDATA%\Python\Scripts` to your User PATH via System &rarr; Environment Variables.

Then restart your terminal and try `pdfwiz --help` again.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Creator: kavehfayyazi
- Email: [kfayyazi@andrew.cmu.edu](mailto:kfayyazi@andrew.cmu.edu)
- Github: [@kavehfayyazi](https://github.com/kavehfayyazi)