import webbrowser
import os

# List of 47 string methods with descriptions and example inputs
string_methods = {
    'lower': ("Converts all characters to lowercase.", "text = 'HELLO'\nprint(text.lower())"),
    'capitalize': ("Converts the first character to uppercase.", "text = 'hello world'\nprint(text.capitalize())"),
    'casefold': ("Returns a casefolded copy of the string.", "text = 'HELLO'\nprint(text.casefold())"),
    'center': ("Centers the string with a specified character.", "text = 'hello'\nprint(text.center(20, '*'))"),
    'encode': ("Encodes the string into bytes.", "text = 'hello'\nprint(text.encode('utf-8'))"),
    'expandtabs': ("Expands tabs in the string into spaces.", "text = 'hello\\thello'\nprint(text.expandtabs(4))"),
    'find': ("Finds the first occurrence of a substring.", "text = 'hello world'\nprint(text.find('world'))"),
    'format': ("Formats the string with placeholders.", "text = 'Hello {name}'\nprint(text.format(name='world'))"),
    'isalnum': ("Checks if all characters are alphanumeric.", "text = 'hello123'\nprint(text.isalnum())"),
    'isalpha': ("Checks if all characters are alphabetic.", "text = 'hello'\nprint(text.isalpha())"),
    'isascii': ("Checks if all characters are ASCII.", "text = 'hello'\nprint(text.isascii())"),
    'isdecimal': ("Checks if all characters are decimals.", "text = '12345'\nprint(text.isdecimal())"),
    'islower': ("Checks if all characters are lowercase.", "text = 'hello'\nprint(text.islower())"),
    'isnumeric': ("Checks if all characters are numeric.", "text = '12345'\nprint(text.isnumeric())"),
    'isupper': ("Checks if all characters are uppercase.", "text = 'HELLO'\nprint(text.isupper())"),
    'ljust': ("Left-justifies the string.", "text = 'hello'\nprint(text.ljust(10, '-'))"),
    'lstrip': ("Removes leading whitespace.", "text = '   hello'\nprint(text.lstrip())"),
    'partition': ("Splits the string into three parts.", "text = 'hello world'\nprint(text.partition(' '))"),
    'rfind': ("Finds the last occurrence of a substring.", "text = 'hello world hello'\nprint(text.rfind('hello'))"),
    'rsplit': ("Splits the string from the right.", "text = 'hello world hello'\nprint(text.rsplit(' ', 1))"),
    'rstrip': ("Removes trailing whitespace.", "text = 'hello   '\nprint(text.rstrip())"),
    'split': ("Splits the string.", "text = 'hello world'\nprint(text.split(' '))"),
    'swapcase': ("Swaps uppercase to lowercase and vice versa.", "text = 'Hello World'\nprint(text.swapcase())"),
    'title': ("Converts to title case.", "text = 'hello world'\nprint(text.title())"),
    'upper': ("Converts all characters to uppercase.", "text = 'hello'\nprint(text.upper())"),
    'zfill': ("Pads the string with zeros.", "text = '42'\nprint(text.zfill(5))"),
    'strip': ("Removes both leading and trailing whitespace.", "text = '   hello   '\nprint(text.strip())"),
    'replace': (
    "Replaces a substring with another substring.", "text = 'hello world'\nprint(text.replace('world', 'Python'))"),
    'count': ("Counts occurrences of a substring.", "text = 'hello world'\nprint(text.count('o'))"),
    'startswith': (
    "Checks if the string starts with a specified prefix.", "text = 'hello world'\nprint(text.startswith('hello'))"),
    'endswith': (
    "Checks if the string ends with a specified suffix.", "text = 'hello world'\nprint(text.endswith('world'))"),
    'index': (
    "Returns the index of the first occurrence of a substring.", "text = 'hello world'\nprint(text.index('world'))"),
    'rindex': ("Returns the index of the last occurrence of a substring.",
               "text = 'hello world world'\nprint(text.rindex('world'))"),
    'join': ("Joins elements of an iterable with the string as a separator.",
             "text = '-'\nprint(text.join(['hello', 'world']))"),
    'splitlines': ("Splits the string at line breaks.", "text = 'hello\\nworld'\nprint(text.splitlines())"),
    'maketrans': ("Creates a mapping table for translations.",
                  "table = str.maketrans('abc', '123')\ntext = 'abc'\nprint(text.translate(table))"),
    'translate': ("Translates the string using a mapping table.",
                  "table = str.maketrans('abc', '123')\ntext = 'abc'\nprint(text.translate(table))"),
    'removeprefix': ("Removes a specified prefix.", "text = 'unhappy'\nprint(text.removeprefix('un'))"),
    'removesuffix': ("Removes a specified suffix.", "text = 'walking'\nprint(text.removesuffix('ing'))"),
    'isascii': ("Checks if all characters in the string are ASCII.", "text = 'hello'\nprint(text.isascii())"),
    'isidentifier': (
    "Checks if the string is a valid identifier.", "text = 'variable_name'\nprint(text.isidentifier())"),
    'isspace': ("Checks if all characters are whitespace.", "text = '   '\nprint(text.isspace())"),
    'istitle': ("Checks if the string follows title case.", "text = 'Hello World'\nprint(text.istitle())"),
}

# Generate HTML content
html_content = '''
<html>
<head>
    <title>Python String Methods & Commands Preview</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            font-size: 16px;
            line-height: 1.6;
            background: url('static/background.jpg') no-repeat center center fixed;
            background-size: cover;
        }
        h1 {
            color: #333;
            font-size: 28px;
            text-align: center;
            margin: 40px 0;
        }
        .method-section {
            margin: 30px auto;
            padding: 20px;
            width: 80%;
            max-width: 1000px;
            background-color: rgba(255, 255, 255, 0.9);  /* Semi-transparent background */
            border: 1px solid #ccc;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        pre {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 14px;
            overflow-x: auto;
        }
        code {
            display: block;
            padding: 10px;
            font-size: 14px;
        }
        .output {
            color: green;
        }
        footer {
            text-align: center;
            margin: 40px 0;
            font-size: 14px;
            color: #777;
        }
    </style>
</head>
<body>
    <h1>Python String Methods & Commands Preview</h1>
'''

# Generate the preview for each method with numbering
for index, (method, (description, code)) in enumerate(string_methods.items(), start=1):
    try:
        # Capture the print output by redirecting stdout
        exec_globals = {}
        exec_locals = {}
        exec(code.replace("Text", "text"), exec_globals, exec_locals)

        # Capturing the last value if no print statement is used
        result = exec_locals.get('text', exec_globals.get('text'))
        if result is None:
            result = "No output"

        html_content += f'''
        <div class="method-section">
            <h2>Method {index}: {method}</h2>
            <p><strong>Description:</strong> {description}</p>
            <pre><code>{code}</code></pre>
            <p><strong>Output:</strong></p>
            <pre class="output"><code># Output: {result}</code></pre>
        </div>
        '''
    except Exception as e:
        # Handle any errors during execution
        html_content += f'''
        <div class="method-section">
            <h2>Method {index}: {method}</h2>
            <p><strong>Description:</strong> {description}</p>
            <pre><code>{code}</code></pre>
            <p><strong>Output:</strong></p>
            <pre class="output"><code># Error: {e}</code></pre>
        </div>
        '''

html_content += '''
    <footer>
        2024 Muhammad Mustafa Saghir. All rights reserved.
    </footer>
</body>
</html>
'''

# Save to HTML file
file_name = 'string_methods_preview.html'
with open(file_name, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Automatically open the HTML file in the default web browser
webbrowser.open(f'file://{os.path.abspath(file_name)}')
