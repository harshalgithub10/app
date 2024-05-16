##IMPORT LIBRARIES
import pandas as pd
import numpy as np

from glob import glob


import matplotlib.pyplot as plt
from PIL import Image

##IMPORT CV2
import cv2

##LOAD A IMAGE
img = cv2.imread('/home/harshu/Downloads/invoice/invoice5.jpg')

##USING IF ELSE CONDITON iMAGE IS SUCSESSSFULLY LOADED OR NOT
if img is None:
    print("Error: Unable to load image.")
else:
    print("Image loaded successfully.")
    
##SHUOWED IMAGE USING MATPLOTLIB AS PLT
plt.imshow(img)

print(type(img))

##IMAGE TYPE CHANGED INTO STRING
img = str(img)

##IMAGE IS SPLITED WITH'/' AND '.'
img = img.split('/')[-1].split('.')

print(img)

##IMPORT PYTESSERACT
import pytesseract
from PIL import Image

##OPEN IMAGE IN JPG
img = Image.open("/home/harshu/Downloads/invoice/invoice5.jpg")

##USING PYTESSERACT CONVERTED IMAGE TO STRING
text = pytesseract.image_to_string(img, lang='eng')

print(text)

import json
import pytesseract
from PIL import Image

# Load the image
img = Image.open('/home/harshu/Downloads/invoice/invoice5.jpg')

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(img, lang='eng')

# Create a dictionary to store the text
text_dict = {
    "text": text
}

# Write the dictionary to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(text_dict, json_file, indent=4)
    
import re
import json

# Define patterns for keys and their corresponding regex patterns
key_patterns = {
    "Bill From": r"Bill From\n(.+?)\n",
    "Ship To": r"Ship To :\n(.+?)\n",
    "Bill To": r"Bill To\n(.+?)\n",
    "Invoice Number": r"INVOICE NUMBER : (.+?) ",
    "Invoice Date": r"INVOICE DATE : (.+?) ",
    "Total Amount": r"Total Amount (.+?)\n",
    "CGST": r"CGST @(.+?)%",
    "SGST": r"SGST @(.+?)%",
    "Grand Total": r"Grand Total (.+?)\n",
    "Due Date": r"Due Date: (.+?)\n",
    "Interest": r"Interest'@ (.+?)%",
    "Document No": r"Document N0 : (.+?)",
    "Document Date" : r"Document Date : (.+?) ",
    "IRN" : r"IRN : (.+?)\n",
    "Generated By" : r"Generated By : (.+?) ",
    "CIN" : r"CIN : (>+?) " ,
    "IGST" : r"IGST : (.+?)",
    "Invoice No" : r"Invoice No : (.+?)\n",
    "State code" : r"State code : (.+?)\n",
    "IGST" : r"IGST : (.+?)",
    "Ack No" : r"Ack No : (.+?)",
    "Ack Date" : r"Ack Date : (.+?)",
    "Document Type" : r"Document Type : (.+?)",
    "invoice_number": r"INVOICE\s+NUMBER\s*:?[^0-9]*([\w/-]+)",
    "invoice_date": r"INVOICE\s+DATE\s*:?[^0-9]*([\d/]+)",
    "total_amount": r"Total\s+Amount[^0-9]*([\d,.]+)",
    "acknowledgement_number": r"£\s*:\s*([^\n]+)",
    "acknowledgement_date": r"CMS\s+conc.*?(\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2})",
    "invoice_number": r"Invoice\s?Number\s?:\s?(\w+)",
    "acknowledgement_number": r"Ack\s?No:\s?(\w+)",
    "acknowledgement_date": r"Ack\s?Date:\s?(\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2})",
    "invoice_date": r"Document\s?Date:\s?(\d{2}-\d{2}-\d{4})",
    "document_number": r"Document\s?No:\s?([^\n]+)",
    "total_amount": r"Total\s?inv\.?\s?([\d,.]+)",
    "supplier_name": r"Details\sof\sSupplier.*?Name:\s?([\w\s]+)",
    "supplier_address": r"Details\sof\sSupplier.*?Address:\s?([\w\s,]+)",
    "supplier_pan": r"Details\sof\sSupplier.*?PANNO:\s?(\w+)",
   "recipient_name": r"Details\sof\sRecipient.*?Name:\s?([\w\s]+)",
    "recipient_address": r"Details\sof\sRecipient.*?Address:\s?([\w\s,]+)",
   "recipient_pan": r"Details\sof\sRecipient.*?PANNO:\s?(\w+)",
   "invoice_number": r"Invoice No./Date\s?:\s?(\d+)\s?/\s?(\d{2}\.\d{2}\.\d{4})",
    "order_number_date": r"Order No./Date\s?:\s?(\d+)\s?/\s?(\d{2}\.\d{2}\.\d{4})",
    "ship_to_party": r"Ship-To Party\s?:\s?([^\n]+)",
    "bill_to_party": r"Bill-To Party\s?:\s?([^\n]+)",
    "lr_number_date": r"LRNo\.\s?:\s?(\d+)\s+LR Date\s?:\s?(\d{2}\.\d{2}\.\d{4})",
    "total_invoice_value": r"TOTAL INVOICE VALUE \(INR\) :[^0-9]*([\d,.]+)",
    "gst_details": r"IGST : ([\d.]+)% ON (\d+)% OF TAXABLE VALUE\s?[\s\n]+: ([\d,.]+)",
    "payment_details": r"Remittance Advice:\s?([^\n]+)",
    "invoice_number": r"Invoice\s?No\.\s?:\s?([^\n]+)",
    "acknowledgement_number": r"Ack\s?No\.\s?:\s?([^\n]+)",
    "acknowledgement_date": r"Ack\s?Date\s?:\s?(\d{2}-[A-Za-z]{3}-\d{2})",
    "invoice_date": r"Document\s?Date\s?:\s?(\d{2}-[A-Za-z]{3}-\d{2})",
    "document_number": r"Delivery\s?Note\s?Mode/Tems\s?of\s?Payment\s?:\s?([^\n]+)",
    "total_amount": r"Total\s?:\s?([\d,.]+)", "invoice_number": r"Invoice\s?No\.\s?:\s?([\w\s-]+)",
    "invoice_date": r"Invoice\s?Date\s?\(d[^\)]*\)\s?(\d{2}-\d{2}-\d{4})",
    "due_date": r"Due\s?Date\s?\(dd-mm-yyyy\)\s?(\d{2}-\d{2}-\d{4})",
    "software_description": r"Sofware\s?Appiication\s?charges\s?for\s?the\s?month\s?of\s?([^\n]+)",
    "amount": r"\|Rate\s?\/\s?Month\s?\u2018Amount\s?\(INR\)\s?([\d,.]+)",
    "igst_percentage": r"IGST\s?([\d.]+)%",
    "total_amount_in_words": r"Amount\s?in\s?words:\s?([\w\s,]+)",
    "total_amount": r"\n([\d,.]+)\n\n\[Bank\s?Information", 
    "invoice_number": r"Invoice\s?No\.\s?:\s?([^[\n]+)",
    "invoice_date": r"Invoice\s?Date\s?\(d[^:]+:\s?(\d{2}-\d{2}-\d{4})",
    "payment_terms": r"Payment\s?Terms\s?:\s?([^[\n]+)",
    "due_date": r"Due\s?Date\s?\(dd-mm-yyyy\)\s?:\s?(\d{2}-\d{2}-\d{4})",
    "po_number": r"PO\s?Rel\.\s?POH\s?:\s?([^[\n]+)",
    "irn_number": r"IRN\s?No\s?:\s?([^[\n]+)",
    "software_charges": r"Sofware\s?Appiication\s?charges\s?:\s?([^[\n]+)",
    "gross_taxable_value": r"Gross\s?Taxable\s?Value\s?:\s?([^[\n]+)",
    "igst": r"IGST\s?:\s?([^[\n]+)",
    "beneficiary_name": r"Beneficiary\s?Name:\s?([^[\n]+)",
    "bank_information": r"Bank\s?Information\s?:\s?([^[\n]+)",
    "statutory_information": r"Our\s?Statutory\s?information\s?:\s?([^[\n]+)",
    "invoice_number": r"Invoice\s?No\.\s?:\s?([^[\n]+)",
     "invoice_number": r"Invoice\s?Number\s?:\s?([^\n]+)",
    "acknowledgement_number": r"Ack\s?No\.\s?:\s?([^\n]+)",
    "acknowledgement_date": r"Ack\s?Date\s?:\s?(\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2})",
    "invoice_date": r"Invoice\s?Date\s?:\s?(\d{2}-\d{2}-\d{4})",
    "document_number": r"Delivery\s?Challan\s?No\.\s?:\s?([^\n]+)",
    "total_amount": r"Total\s?Amount\s?([\d,.]+)",
    "invoice_number": r"Invoice\s?No(?:\.|umber)?\s?:\s?([^\n]+)",
    "acknowledgement_number": r"Ack(?:\.|nowledgment)\s?No(?:\.|umber)?\s?:\s?([^\n]+)",
    "acknowledgement_date": r"Ack(?:\.|nowledgment)\s?Date\s?:\s?([\d\-]+)",
    "invoice_date": r"Invoice\s?Date\s?:\s?([\d\-]+)",
    "document_number": r"Invoice\s?No(?:\.|umber)?\s?Dated\s?:\s?([^\n]+)",
    "total_amount": r"Amount Chargeable\s?\(in\s?words\)\s?:\s?([^\n]+)",
    "invoice_number": r"Invoice\s?No(?:\.|umber)?\s?:\s?([^\n]+)",
    "acknowledgement_number": r"Ack(?:\.|nowledgment)\s?No(?:\.|umber)?\s?:\s?([^\n]+)",
    "acknowledgement_date": r"Ack(?:\.|nowledgment)\s?Date\s?:\s?([\d\-]+)",
    "invoice_date": r"Invoice\s?Date\s?:\s?([\d\-]+)",
    "document_number": r"Invoice\s?No(?:\.|umber)?\s?Dated\s?:\s?([^\n]+)",
    "total_amount": r"Amount Chargeable\s?\(in\s?words\)\s?:\s?([^\n]+)",
    "invoice_number": r"Invoiee\s?No\.\s?:\s?(\d+)",
    "invoice_date": r"PO\s?Date\s?([\d.]+)",
    "document_number": r"Material\s?Description\s?HSN\/\s?Discount\s?Other\s?Taxable\s?CGST\s?CGST\s?SGST\s?SGST\s?IGST\s?IGST\s?(?:\d+\s?)*\|\s?(\w+)\s",
    "total_amount": r"Total\s?Amount\s?([\d.,]+)",
    "invoice_number": r"Invoice\s?No(?:\.|umber) ?: ?([^,]+)",
    "acknowledgement_number": r"Ack\s?No(?:\.|umber) ?: ?([^,]+)",
    "acknowledgement_date": r"Ack\s?Date ?: ?(\d{2}-[a-zA-Z]{3}-\d{2})",
    "invoice_date": r"Dated ?: ?(\d{2}-[a-zA-Z]{3}-\d{2})",
    "document_number": r"Dispatch\s?Doc\s?No(?:\.|umber) ?: ?([^,]+)",
    "total_amount": r"Total\s?Amount(?:\sin\s?words) ?: ?([^,]+)",
     "invoice_ref_number": r"Invoice\s?Ref\.\s?No\s?:\s?(\w+)",
    "invoice_date": r"Date\s?:\s?(\d{2}/\d{2}/\d{4})",
    "customer_order_ref_number": r"Customer's\s?Order\s?Ref\.\s?No\.\s?:\s?(\w+)",
    "customer_order_date": r"Customer's\s?Order\s?Date\s?:\s?(\d{2}/\d{2}/\d{4})",
    "total_taxable_value": r"Total\s?Taxable\s?Value\s?:\s?([\d,.]+)",
    "total_tax_amount": r"Total\s?Tax\s?Amount\s?:\s?([\d,.]+)",
    "remarks": r"Remarks\s?:\s?(.*)",
    "invoice_number": r"Invoice\s?No\.\s?:\s?([^\n]+)",
    "invoice_date": r"Invoice\s?Date\s?:\s?(\d{2}\.\d{2}\.\d{4})",
    "bill_to_party": r"Bill-to Party:\n([^\n]+)",
    "ship_to_party": r"Ship-to Party:\n([^\n]+)",
    "total_amount": r"Total\s?:\s?([\d,.]+)",
    "invoice_number": r"Invoice\s?Number\s?:\s?([^\n]+)",
    "acknowledgement_number": r"Ack\s?No\s?:\s?(\d+)",
    "acknowledgement_date": r"Ack\s?Date\s?:\s?(\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2})",
    "invoice_date": r"Document\s?Date\s?:\s?(\d{2}-\d{2}-\d{4})",
    "document_number": r"Document\s?No\s?:\s?([^\n]+)",
    "total_amount": r"Total\s?inv\.\s?Amt\s?:\s?([\d,.]+)",
    "invoice_number": r"Invoice\s?No\.\s?:\s?([\w/-]+)",
    "acknowledgement_number": r"Ack\s?No\.\s?:\s?([^\n]+)",
    "acknowledgement_date": r"Ack\s?Date\s?:\s?(\d{2}-[a-zA-Z]{3}-\d{2})",
    "invoice_date": r"Invoice\s?Date\s?:\s?(\d{2}-[a-zA-Z]{3}-\d{2})",
    "document_number": r"Delivery\s?Note\s?:\s?([\w/-]+)",
    "total_amount": r"Total\s?INR\s?([\d,/.]+)",
    "invoice_number": r"Invoice\s?No\s?:\s?([^\n]+)",
    "acknowledgement_number": r"Ack\s?No\s?:\s?([^\n]+)",
    "acknowledgement_date": r"Ack\s?Date\s?:\s?(\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2})",
    "invoice_date": r"Invoice\s?Date\s?:\s?(\d{2}-\d{2}-\d{4})",
    "document_description": r"Description:\s?([^\n]+)",
    "total_amount": r"Total\s?Amt\s?:\s?([\d,.]+)",
    "supplier_name": r"Details\sof\sSupplier:\sName:\s([^\n]+)",
    "recipient_name": r"Recipient\sName:\s([^\n]+)",
    "supplier_address": r"Address:\s([^\n]+)",
    "recipient_address": r"Address:\s([^\n]+)",
    "supplier_gstin": r"GSTINNO:\s([^\n]+)",
    "recipient_gstin": r"GSTINNO:\s([^\n]+)",
     "invoice_number": r"Invoice\s?No\./Date\s?:\s?([^\n]+)",
    "invoice_date": r"Invoice\s?No\./Date\s?:\s?.*?(\d{2}\.\d{2}\.\d{4})",
    "total_amount": r"TOTAL\s?INVOICE\s?VALUE\s?\(INR\)\s?:\s?([^\n]+)",
    "acknowledgement_number": r"LRNo\.\s?:\s?([^\n]+)",
    "acknowledgement_date": r"LR Date\s?:\s?(\d{2}\.\d{2}\.\d{4})",
    "document_number": r"Order\s?No\./Date\s?:\s?([^\n]+)", 
     "invoice_number": r"INVOICE\s?NUMBER\s?:\s?([\w/]+)",
    "invoice_date": r"INVOICE\s?DATE\s?(\d{2}/\d{2}/\d{4})",
    "total_amount": r"Total\s?Amount\s?([\d,]+\.\d{2})",
    "due_date": r"Due\s?Date:\s?(\d{2}/\d{2}/\d{4})",
    "acknowledgement_date": r"\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}",
    "acknowledgement_number": r"Ack\s?No\.\s?:\s?([^\n]+)",
    "document_number": r"Document\s?No\.\s?:\s?([^\n]+)",
}

# Extract values corresponding to keys using regular expressions
data = {}
for key, pattern in key_patterns.items():
    match = re.search(pattern, text)
    if match:
        data[key] = match.group(1).strip()

# Write the extracted data to a JSON file
output_file = 'invoice_details.json'
with open(output_file, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Invoice details have been extracted and saved to 'invoice_details.json'")