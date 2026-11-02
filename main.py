
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from parser import parse_classes
from wmc import calculate_wmc
from cohesion import calculate_cohesion
from coupling import calculate_coupling
from rfc import calculate_rfc


def analyze_code():
    source_code = code_input.get("1.0", tk.END)

    if not source_code.strip():
        messagebox.showwarning("Missing Code", "Please paste or upload Python code.")
        return

    try:
        classes = parse_classes(source_code)

        if not classes:
            messagebox.showinfo("No Classes", "No Python classes were found.")
            return

        results.delete("1.0", tk.END)

        results.insert(tk.END, "OBJECT-ORIENTED METRIC RESULTS\n")
        results.insert(tk.END, "=" * 40 + "\n")

        for cls in classes:
            wmc = calculate_wmc(cls)
            cohesion = calculate_cohesion(cls)
            coupling = calculate_coupling(cls)
            rfc = calculate_rfc(cls)

            results.insert(tk.END, f"\nClass: {cls['name']}\n")
            results.insert(tk.END, f"Methods: {cls['methods']}\n")
            results.insert(tk.END, f"WMC: {wmc}\n")
            results.insert(
                tk.END,
                f"Cohesion (TCC): {cohesion if cohesion is not None else 'N/A'}\n"
            )
            results.insert(tk.END, f"Coupling (CBO): {coupling}\n")
            results.insert(tk.END, f"Dependencies: {cls['dependencies']}\n")
            results.insert(tk.END, f"RFC: {rfc}\n")
            results.insert(tk.END, "-" * 40 + "\n")

    except SyntaxError as error:
        messagebox.showerror(
            "Syntax Error",
            f"Invalid Python code:\n{error}"
        )


def upload_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                code = file.read()

            code_input.delete("1.0", tk.END)
            code_input.insert(tk.END, code)

        except OSError as error:
            messagebox.showerror("File Error", str(error))


# Create main window
root = tk.Tk()
root.title("OO Metric Tool")
root.geometry("850x750")

# Heading
heading = tk.Label(
    root,
    text="Object-Oriented Metric Tool",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

# Instructions
instructions = tk.Label(
    root,
    text="Upload a Python file or paste Python class definitions below."
)
instructions.pack()

# Code input
code_input = scrolledtext.ScrolledText(
    root,
    height=15,
    width=95,
    font=("Consolas", 10)
)
code_input.pack(padx=10, pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

upload_button = tk.Button(
    button_frame,
    text="Upload Python File",
    command=upload_file
)
upload_button.pack(side=tk.LEFT, padx=10)

analyze_button = tk.Button(
    button_frame,
    text="Analyze Code",
    command=analyze_code
)
analyze_button.pack(side=tk.LEFT, padx=10)

# Results heading
results_heading = tk.Label(
    root,
    text="Metric Results",
    font=("Arial", 14, "bold")
)
results_heading.pack(pady=5)

# Results display
results = scrolledtext.ScrolledText(
    root,
    height=18,
    width=95,
    font=("Consolas", 10)
)
results.pack(padx=10, pady=10)

# Start application
root.mainloop()
