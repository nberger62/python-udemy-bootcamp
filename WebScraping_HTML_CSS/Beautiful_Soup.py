# BeautifulSoup(html_string, "html.parser") - parse HTML

# Parse the Tag name, use the method called find, or find_all, Navigate with CSS

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bread Recipe</title>
    <style type=""text/css">
        h1{
            color: red;
            background: black;
        }
        li {
            color: red;
            font-size: 20px;
        }
        #first {
            color: blue;
        }


    </style>
</head>
<body>
    <h1>Sf Sourdough Loaf</h1>
    <em>WRITTEN BY Nathan Berger</em>
    <h3>Ingredients</h3>
    <ul>
        <li id="first">Flour</li>
        <li>Water</li>
        <li>Yeast</li>
    </ul>

Sourdough Starter


</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
d = soup.select("#first") # Navigating with CSS
# find and find_all are not CSS
print(d)


# soup.find, soup.select, soup.find_all, soup.find



