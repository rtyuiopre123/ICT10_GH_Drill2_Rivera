from pyscript import document

def area_triangle(base, height):
    return (base * height) / 2

def compute_area(event):

    base = float(document.getElementById("base").value)
    height = float(document.getElementById("height").value)

    area = area_triangle(base, height)

    output = f"""
    Base: {base} <br>
    Height: {height} <br>
    Area of Triangle: {area}
    """

    document.getElementById("display").innerHTML = output