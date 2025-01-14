# Hunter SDK Service

This project is a simple SDK service for the Hunter API with in-memory data storage and a service layer. It uses `wemake-python-styleguide` for linting and follows strict coding standards.

## Project Structure
sdk_service/ ├── hunter_sdk/ │ ├── init.py │ ├── client.py │ ├── storage.py │ └── service.py ├── tests/ │ ├── init.py │ └── test_service.py ├── setup.cfg └── main.py

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/satoterin/Python_SDK_Service.git
    ```

2. Install `requirements`:
    ```sh
    pip install -r requirements.txt
    ```
    or manually
    ```sh
    pip install mypy wemake-python-styleguide requests types-requests
    ```

## Configuration

The [setup.cfg](http://_vscodecontentref_/3) file is configured to use `wemake-python-styleguide` and `mypy` for linting and type checking.

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```

2. Run the linter:
    ```sh
    flake8 . --select=WPS
    ```

3. Run the type checker:
    ```sh
    mypy sdk_service
    ```