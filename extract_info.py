import ast

def extract_information_from_code(code):
    # Parse the code into an abstract syntax tree (AST)
    tree = ast.parse(code)

    # Initialize lists to store extracted information
    function_names = []
    variable_names = []
    comments = []
    docstrings = []

    # Define a NodeVisitor subclass to traverse the AST and extract information
    class CodeVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            # Extract function names
            function_names.append(node.name)
            self.generic_visit(node)

        def visit_Name(self, node):
            # Extract variable names
            if isinstance(node.ctx, ast.Store):
                variable_names.append(node.id)
            self.generic_visit(node)

        def visit_Comment(self, node):
            # Extract comments
            comments.append(node.value.strip())
            self.generic_visit(node)

        def visit_Str(self, node):
            # Extract docstrings
                docstring = ast.get_docstring(node)
                if docstring is not None:
                    docstrings.append(docstring)
                self.generic_visit(node)

    # Instantiate the CodeVisitor and traverse the AST
    visitor = CodeVisitor()
    visitor.visit(tree)

    # Return the extracted information
    return {
        "function_names": function_names,
        "variable_names": variable_names,
        "comments": comments,
        "docstrings": docstrings
    }

# Example code to parse
code = """
# This is a comment
def example_function():
    \"\"\"This is a docstring.\"\"\"
    variable = 123
"""

# Extract information from the code
information = extract_information_from_code(code)

# Print the extracted information
print("Function names:", information["function_names"])
print("Variable names:", information["variable_names"])
print("Comments:", information["comments"])
print("Docstrings:", information["docstrings"])
