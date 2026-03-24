# Outreachy Wikimedia Foundation - Microtasks

This repository contains my completed microtasks for the **Outreachy May 2026 Internship** with **Wikimedia Foundation**.

**Project:** Addressing the lusophone technological wishlist proposals  
**Applicant:** Ibrahim Jamiu 
**GitHub:** Olawoyin365

---

## Project Overview

This project aims to implement community wishes from the Lusophone technological wishlist, specifically:
- **Wish #3:** Implement a check in the Visual Editor for duplicate references
- **Wish #8:** Implement Wikidata support for Wikimedia Brasil's scoring tool (wikiscore)

During the contribution period, I completed two microtasks demonstrating my technical skills in JavaScript and Python.

---

## Repository Contents

```
outreachy-wikimedia-tasks/
├── Task 1 Intern.html                 # JavaScript date formatter
├── Task 2 - Intern.csv                # Input CSV file with URLs
├── task_2_url_status_checker.py       # Python URL status checker
└── README.md                          # This file
```

---

## Task 1: JavaScript Date Formatter

### Objective
Create a JavaScript script to manipulate a JSON object and print article information in a human-legible format.

### Requirements
- Read JSON data containing Wikipedia article information
- Format creation dates from ISO format (YYYY-MM-DD) to readable format (Month Day, Year)
- Display results in the format: `Article "TITLE" (Page ID XXXXX) was created at Month Day, Year.`

### Implementation

**File:** `Task 1 Intern.html`

**Key Features:**
- Date parsing and formatting using JavaScript `Date` object
- Array iteration with `forEach()` to process 12 articles
- DOM manipulation to display formatted results
- Modular code design with reusable `formatDate()` function

**Code Highlights:**
```javascript
// Function to convert date string to human-readable format
function formatDate(dateString) {
    const date = new Date(dateString);
    const months = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"];
    const month = months[date.getMonth()];
    const day = date.getDate();
    const year = date.getFullYear();
    return month + " " + day + ", " + year;
}
```

### Testing & Results

**How to Test:**
1. Open `Task_1_Intern.html` in any modern web browser
2. Verify that both code and results sections are populated

**Expected Output:**
```
Article "André Baniwa" (Page ID 6682420) was created at September 13, 2021.
Article "Benki Piyãko" (Page ID 4246775) was created at December 10, 2013.
Article "Célia Xakriabá" (Page ID 5882073) was created at December 3, 2018.
Article "Chirley Pankará" (Page ID 6977673) was created at October 5, 2022.
Article "Cristine Takuá" (Page ID 7069044) was created at February 16, 2023.
Article "Eliane Potiguara" (Page ID 2119511) was created at January 28, 2009.
Article "Jaider Esbell" (Page ID 6714407) was created at October 9, 2021.
Article "Jerônimo Rodrigues" (Page ID 6977117) was created at October 4, 2022.
Article "Nanblá Gakran" (Page ID 6935831) was created at August 2, 2022.
Article "Sônia Guajajara" (Page ID 4908665) was created at November 13, 2015.
Article "Vãngri Kaingáng" (Page ID 5886895) was created at December 12, 2018.
Article "Zezico Guajajara" (Page ID 6549130) was created at April 10, 2021.
```

**Test Results:**  **PASSED**
- All 12 articles formatted correctly
- Dates properly converted from ISO format to human-readable format
- Output matches required format specification

---

## Task 2: Python URL Status Checker

### Objective
Create a Python script to read URLs from a CSV file and print their HTTP status codes.

### Requirements
- Read URLs from the provided CSV file (`Task 2 - Intern.csv`)
- Make HTTP requests to each URL
- Print status codes in the format: `(STATUS CODE) URL`

### Implementation

**File:** `task_2_url_status_checker.py`

**Key Features:**
- CSV file reading with proper encoding handling (UTF-8-sig for BOM)
- HTTP requests using the `requests` library
- Comprehensive error handling for network issues (timeouts, connection errors)
- User-agent headers to avoid being blocked by websites
- Progress tracking for large URL lists
- Type hints for better code documentation

**Code Highlights:**
```python
def get_status_code(url: str) -> Tuple[int, str]:
    """Get the HTTP status code for a given URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, timeout=10, headers=headers, allow_redirects=True)
        return (response.status_code, url)
    except requests.exceptions.Timeout:
        return (408, url)  # Request Timeout
    except requests.exceptions.ConnectionError:
        return (503, url)  # Service Unavailable
    except requests.exceptions.RequestException:
        return (500, url)  # Internal Server Error
```

### Testing & Results

**Prerequisites:**
```bash
pip install requests
```

**How to Test:**
```bash
python task_2_url_status_checker.py
```

**Test Environment:**
- Python 3.x
- Windows Git Bash / macOS Terminal / Linux Shell
- Internet connection required

**Sample Output:**
```
Reading URLs from 'Task 2 - Intern.csv'...

CSV Header detected: 'uls'
Column names found: ['uls']

Found 166 URLs. Starting status code checks...
This may take a few minutes...

====================================================================================================
(503) http://jogandocomelas.com.br/rosana-augusto-jogadora-do-santos-e-da-selecao-brasileira...
(503) http://maquinadoesporte.uol.com.br/artigo/por-time-feminino-corinthians-faz-parceria...
(200) http://sportv.globo.com/site/noticia/2011/11/em-casa-sao-jose-vence-colo-colo-e-e-campeao...
(404) http://www.ecuafutbol.org/copa_america/team.aspx?ID=BRA
(200) https://agenciabrasil.ebc.com.br/esportes/noticia/2020-02/bia-zaneratto-chega-ao-palmeiras...
--- Processed 20/166 URLs ---
...
--- Processed 160/166 URLs ---
====================================================================================================

Completed checking 166 URLs.
```

**Status Code Summary:**
- **200** - OK (page exists and loaded successfully)
- **404** - Not Found (page doesn't exist)
- **408** - Request Timeout (server took too long to respond)
- **503** - Service Unavailable (server down or blocking requests)
- **500** - Internal Server Error (generic error)

**Test Results:** **PASSED**
- Successfully processed all 166 URLs from CSV file
- Proper error handling for various network conditions
- Output format matches requirements: `(STATUS CODE) URL`
- Script handles encoding issues (BOM in CSV file)

---

##  Technologies Used

### Task 1
- **HTML5** - Document structure
- **JavaScript (ES6)** - Date manipulation and DOM interaction
- **CSS3** - Styling and layout

### Task 2
- **Python 3.x** - Core programming language
- **requests library** - HTTP requests
- **csv module** - CSV file parsing
- **typing module** - Type hints for code clarity

---

## Development Notes

### Challenges Encountered

**Task 1:**
- Initial issue with file encoding causing syntax errors
- Resolved by creating a clean HTML file with proper structure
- Ensured cross-browser compatibility by using standard JavaScript (no arrow functions)

**Task 2:**
- CSV file had BOM (Byte Order Mark) causing header reading issues
- Implemented multiple encoding fallback (UTF-8-sig, UTF-8, latin-1, cp1252)
- Added flexible column detection to handle variations in CSV structure
- Some URLs are slow or unresponsive, requiring timeout handling

### Best Practices Applied

Clean, readable code with comprehensive comments  
Modular functions for reusability  
Comprehensive error handling  
Type hints in Python for better code documentation  
Progress indicators for long-running operations  
Follows requirements specification exactly

---

## 🚀 How to Run

### Task 1: JavaScript Date Formatter

1. Navigate to the repository folder
2. Open `Task 1 Intern.html` in any web browser
3. View the formatted output in the "Results of my code" section

**No installation required!**

### Task 2: Python URL Status Checker

1. Ensure Python 3.x is installed
2. Install required dependency:
   ```bash
   pip install requests
   ```
3. Ensure `Task 2 - Intern.csv` is in the same directory
4. Run the script:
   ```bash
   python task_2_url_status_checker.py
   ```
5. Wait for all URLs to be checked (approximately 5-15 minutes)

---

## Submission Information

**Submitted to:** tecnologia@wmnobrasil.org  
**Subject:** [Outreachy] Ibrahim  
**Submission Date:** Tuesday 24th March 2026

**Mentors:**
- Artur Corrêa Souza (WMB) - GitHub: [@arcstur](https://github.com/arcstur)
- Éder Porto - GitHub: [@Ederporto](https://github.com/Ederporto)

---

---

This project is created as part of the Outreachy application process for Wikimedia Foundation.

---

Thank you to the Wikimedia Foundation and Wikimedia Brasil for this opportunity, and to my mentors Artur and Éder for their guidance and detailed task instructions during the contribution period.

---

**Status:**  Both microtasks completed and tested successfully  
**Last Updated:** Tuesday 24th March, 2026
