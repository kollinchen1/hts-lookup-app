# HTS Lookup Web App

This app allows users to input a part number and fetch HTS information from Advantech's SAP API.

## Tech Stack
- Flask (Python backend)
- HTML/JavaScript frontend
- Hosted on Render (free tier)

## Deployment (Render)

1. Push this project to GitHub
2. Go to https://render.com → New Web Service
3. Connect your GitHub repo
4. Set:
   - Build command: pip install -r requirements.txt
   - Start command: python app.py

5. You’ll get a public URL

## API Reference

This app proxies:
GET https://sapapi.advantech.com/api/Materials/GetMaterialImportExportData?salesOrg=US01&partNumber={part}

Returns:
- HTS code
- COO
- HTS Description
