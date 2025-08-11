# Copilot Instructions for RandomDataGenerator

## Repository Overview

**RandomDataGenerator** is a lightweight Python library that generates random user data using the random-data-api.com API. The library provides a simple interface to retrieve random user information in various formats (list, set, dict) for testing and development purposes.

**Repository Stats:**
- **Size:** Small (3 Python files)
- **Language:** Python 3.12+ 
- **Framework:** None (pure Python with requests dependency)
- **Type:** Utility library
- **Dependencies:** `requests` library only

## Build and Testing Instructions

### Prerequisites
- Python 3.12+ (tested with Python 3.12.3)
- `requests` library (version 2.31.0 or compatible)

### Environment Setup
**ALWAYS install requests before running the code:**
```bash
pip install requests
```

### Running the Code
The library can be imported and used directly:
```bash
cd /path/to/repository
python3 -c "from DataGenerator import RandomDataGenerator; print('Import successful')"
```

### Testing
**IMPORTANT:** Tests require internet connectivity to random-data-api.com and may fail in sandboxed environments.

**Known Issues with Tests:**
1. **Network Dependency:** Tests fail with DNS resolution errors when external connectivity is unavailable
2. **URL Construction Bug:** The API URL gets corrupted after multiple calls due to improper string concatenation in line 17 of DataGenerator.py
3. **Error:** `socket.gaierror: [Errno -5] No address associated with hostname` is common

**To run tests (may fail in offline environments):**
```bash
python3 -m unittest test_DataGenerator -v
```

**Syntax Validation (always works):**
```bash
python3 -m py_compile DataGenerator.py test_DataGenerator.py
```

### Build Commands
No build step required - this is pure Python. For validation:
```bash
# Syntax check only
python3 -m py_compile *.py

# Import test
python3 -c "from DataGenerator import RandomDataGenerator"
```

**Time Requirements:**
- Syntax validation: <1 second
- Import test: <1 second  
- Unit tests: 5-60 seconds (depends on network, often fails with timeout)

## Project Layout and Architecture

### File Structure
```
/
├── DataGenerator.py          # Main library class (49 lines)
├── test_DataGenerator.py     # Unit tests (45 lines)
├── README.md                 # Usage documentation
├── .gitignore               # Python gitignore rules
└── .github/
    └── copilot-instructions.md  # This file
```

### Key Source Files

**DataGenerator.py** - Main library implementation:
- `RandomDataGenerator` class with static methods
- `get_users(data_type="list", length=5)` - Main public method
- `__connect_to_api()` - Private method for API communication
- **Known Bug:** Line 17 has improper URL concatenation causing malformed URLs

**test_DataGenerator.py** - Unit tests:
- 8 test methods covering different data types and edge cases
- Tests data validation, type checking, and error handling
- **Requires network connectivity** - will fail offline

### Architecture
- **Pattern:** Simple utility class with static methods
- **API Integration:** REST API calls to random-data-api.com
- **Data Processing:** JSON response parsing and transformation
- **Error Handling:** Basic exception handling for network issues

### Configuration Files
**None present** - No linting config, CI/CD, requirements.txt, or setup.py files exist.

### Dependencies
- **Runtime:** `requests` library (HTTP client)
- **Standard Library:** `json`, `time` modules
- **Development:** `unittest` (built-in testing framework)

## Validation and Checks

### Manual Validation Steps
1. **Syntax Check:** `python3 -m py_compile *.py`
2. **Import Test:** `python3 -c "from DataGenerator import RandomDataGenerator"`
3. **Method Signature:** Verify `get_users()` method exists and accepts `data_type` and `length` parameters

### No Automated CI/CD
- No GitHub Actions workflows
- No pre-commit hooks
- No automated linting or formatting
- No dependency scanning

### Common Issues and Workarounds
1. **URL Corruption Bug:** The `__api_url` gets modified incorrectly on line 17. Each call appends `?size=N` without resetting the base URL.
   
2. **Network Failures:** Tests will fail in sandboxed environments. This is expected behavior.

3. **Missing Dependencies:** If `requests` is not installed, imports will fail with `ModuleNotFoundError`.

### File Contents Reference

**README.md highlights:**
- Import statement: `from DataGenerator import RandomDataGenerator`
- Basic usage: `data = RandomDataGenerator.get_users()`
- Supports data_type: "list", "set", "dict"
- Default length: 5, max length: 10

**Main method signature:**
```python
@staticmethod
def get_users(data_type="list", length=5):
```

## Agent Instructions

**TRUST THESE INSTRUCTIONS** - Only search for additional information if these instructions are incomplete or incorrect.

**For code changes:**
1. Always run syntax validation before committing
2. The URL bug in line 17 should be fixed if making API-related changes
3. Tests will likely fail due to network issues - this is not necessarily a code problem
4. No build tools or linters are configured - manual code review is required
5. All functionality is in the root directory - no subdirectories to navigate

**For testing:**
1. Always test imports first: `python3 -c "from DataGenerator import RandomDataGenerator"`
2. Unit tests require internet access and may timeout
3. Consider mocking the API for reliable testing in sandboxed environments