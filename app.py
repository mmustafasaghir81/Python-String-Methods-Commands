from flask import Flask, render_template, request

app = Flask(__name__)

# List of 46 string methods and outputs
def string_methods():
    text = "Welcome to PIACI Institute"
    methods = [
        {"method": "upper()", "output": text.upper()},
        {"method": "lower()", "output": text.lower()},
        {"method": "capitalize()", "output": text.capitalize()},
        {"method": "title()", "output": text.title()},
        {"method": "swapcase()", "output": text.swapcase()},
        {"method": "strip()", "output": text.strip()},
        {"method": "lstrip()", "output": text.lstrip()},
        {"method": "rstrip()", "output": text.rstrip()},
        {"method": "replace('PIACI', 'Tech')", "output": text.replace("PIACI", "Tech")},
        {"method": "find('PIACI')", "output": text.find("PIACI")},
        {"method": "rfind('PIACI')", "output": text.rfind("PIACI")},
        {"method": "index('PIACI')", "output": text.index("PIACI")},
        {"method": "rindex('PIACI')", "output": text.rindex("PIACI")},
        {"method": "split()", "output": text.split()},
        {"method": "rsplit()", "output": text.rsplit()},
        {"method": "join(['Welcome', 'to', 'PIACI', 'Institute'])", "output": " ".join(['Welcome', 'to', 'PIACI', 'Institute'])},
        {"method": "startswith('Welcome')", "output": text.startswith("Welcome")},
        {"method": "endswith('Institute')", "output": text.endswith("Institute")},
        {"method": "islower()", "output": text.islower()},
        {"method": "isupper()", "output": text.isupper()},
        {"method": "istitle()", "output": text.istitle()},
        {"method": "isdigit()", "output": text.isdigit()},
        {"method": "isalpha()", "output": text.isalpha()},
        {"method": "isalnum()", "output": text.isalnum()},
        {"method": "isspace()", "output": text.isspace()},
        {"method": "isnumeric()", "output": text.isnumeric()},
        {"method": "isdecimal()", "output": text.isdecimal()},
        {"method": "isprintable()", "output": text.isprintable()},
        {"method": "isidentifier()", "output": text.isidentifier()},
        {"method": "zfill(30)", "output": text.zfill(30)},
        {"method": "ljust(30)", "output": text.ljust(30)},
        {"method": "rjust(30)", "output": text.rjust(30)},
        {"method": "center(30)", "output": text.center(30)},
        {"method": "encode()", "output": str(text.encode())},  # Proper encoding output with str()
        {"method": "expandtabs(4)", "output": "Hello\tWorld".expandtabs(4)},
        {"method": "partition('to')", "output": text.partition("to")},
        {"method": "rpartition('to')", "output": text.rpartition("to")},
        {"method": "casefold()", "output": text.casefold()},
        {"method": "format('PIACI')", "output": "Welcome to {}".format("PIACI")},
        {"method": "format_map()", "output": "{name} is learning".format_map({'name': 'John'})},
        {"method": "translate(str.maketrans('PIACI', 'ABCDE'))", "output": text.translate(str.maketrans("PIACI", "ABCDE"))},
        {"method": "count('o')", "output": text.count("o")},
        {"method": "splitlines()", "output": text.splitlines()},  # Correct output for splitlines
        {"method": "rsplit(' ', 1)", "output": text.rsplit(' ', 1)},
        {"method": "rstrip('Institute')", "output": text.rstrip('Institute')},
        {"method": "lstrip('Welcome')", "output": text.lstrip('Welcome')}
    ]
    return methods

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Preview route with pagination
@app.route('/preview')
def preview():
    methods = string_methods()
    
    # Get the page number from the query parameter; default is page 1
    page = int(request.args.get('page', 1))
    per_page = 10  # Show 10 methods per page
    total_pages = (len(methods) + per_page - 1) // per_page  # Calculate total pages
    
    # Calculate start and end index for the current page
    start = (page - 1) * per_page
    end = start + per_page
    methods_page = methods[start:end]
    
    return render_template('preview.html', methods=methods_page, page=page, total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)
