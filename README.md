# Vehicle Registration Form

A desktop application built with Python and Tkinter that implements a vehicle registration form with regex-based input validation. Validation logic is fully decoupled into a separate class.

## Requirements

- Python 3.x
- Tkinter (included in the standard Python distribution)

## Project Structure

```
.
├── registro_vehiculo.py   # Main application and GUI
├── validacion.py          # Validation class (regex methods)
└── README.md
```

## Running the Application

```bash
python registro_vehiculo.py
```

Both files must be in the same directory.

## Form Fields

| Field | Validation Rule |
|---|---|
| Plate | Colombian format: 3 letters + 2 digits + 1 alphanumeric character (e.g. ABC123, ABC12D) |
| Brand | Letters and spaces only |
| Model (year) | Valid year between 1900 and 2026 |
| Color | Letters and spaces only |
| Chassis number | Exactly 17 alphanumeric characters |
| Engine number | Alphanumeric characters |
| ID number | 7 to 10 digits |
| Owner name | Letters and spaces only |
| Email | Standard email format (e.g. user@domain.com) |
| Phone | Exactly 10 digits |

## Validation Class

`validacion.py` contains the `Validacion` class with one method per field. All methods follow the same signature: they receive a string and return a boolean.

```python
Validacion.validar_placa("ABC123")    # True
Validacion.validar_correo("x@y.com") # True
Validacion.validar_cedula("123")      # False
```

## Behavior

- Invalid field: highlighted in red with an error message below the input.
- Valid field: highlighted in green with a confirmation indicator.
- All fields valid: success dialog is shown and the form is cleared.

## Regular Expressions Used

| Method | Pattern | Description |
|---|---|---|
| validar_placa | `^[A-Z]{3}[0-9]{2}[0-9A-Z]$` | 3 uppercase letters, 2 digits, 1 digit or letter |
| validar_marca | `^[a-zA-Z ]+$` | One or more letters and spaces |
| validar_modelo | `^(19[0-9]{2}\|200[0-9]\|201[0-9]\|202[0-6])$` | Year range 1900-2026 |
| validar_color | `^[a-zA-Z ]+$` | One or more letters and spaces |
| validar_chasis | `^[a-zA-Z0-9]{17}$` | Exactly 17 alphanumeric characters |
| validar_noMotor | `^[a-zA-Z0-9]+$` | One or more alphanumeric characters |
| validar_cedula | `^[0-9]{7,10}$` | 7 to 10 digits |
| validar_nombre | `^[a-zA-Z ]+$` | One or more letters and spaces |
| validar_correo | `^[\w.+\-]+@[\w\-]+\.[a-zA-Z]{2,}$` | Standard email format |
| validar_telefono | `^[0-9]{10}$` | Exactly 10 digits |
