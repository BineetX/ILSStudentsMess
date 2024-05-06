from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Function to create a PDF invoice
def create_invoice(invoice_number, customer_name, items):
    # Create a canvas with specified page size (A4)
    c = canvas.Canvas(f"Invoice_{invoice_number}.pdf", pagesize=A4)

    # Set font styles
    c.setFont("Helvetica", 12)
    c.setFont("Helvetica-Bold", 14)

    # Write invoice header
    c.drawString(50, 750, "Invoice")
    c.setFont("Helvetica", 10)
    c.drawString(50, 730, f"Invoice Number: {invoice_number}")
    c.drawString(50, 710, f"Customer Name: {customer_name}")
    c.setFont("Helvetica-Bold", 12)

    # Write table header
    c.drawString(50, 680, "Item")
    c.drawString(200, 680, "Quantity")
    c.drawString(300, 680, "Price")
    c.line(50, 675, 450, 675)

    # Write table rows
    row_height = 30
    y = 650
    total_amount = 0

    for item in items:
        c.drawString(50, y, item["name"])
        c.drawString(200, y, str(item["quantity"]))
        c.drawString(300, y, str(item["price"]))
        total_amount += item["quantity"] * item["price"]
        y -= row_height

    # Write total amount
    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, y, "Total Amount:")
    c.drawString(300, y, str(total_amount))

    # Save the PDF file
    c.save()
    print(f"Invoice_{invoice_number}.pdf created successfully.")

# Example usage
invoice_number = "INV001"
customer_name = "John Doe"
items = [
    {"name": "Product 1", "quantity": 2, "price": 10},
    {"name": "Product 2", "quantity": 1, "price": 15},
    {"name": "Product 3", "quantity": 3, "price": 8},
]

create_invoice(invoice_number, customer_name, items)