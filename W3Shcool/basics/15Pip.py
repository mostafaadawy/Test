# Python PIP
# PIP is a package manager for Python packages, or modules if you like.
# Note: If you have Python version 3.4 or later, PIP is included by default.

# pip install camelcase


import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

# Remove a Package
# pip uninstall camelcase
